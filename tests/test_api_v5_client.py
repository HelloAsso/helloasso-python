from unittest.mock import Mock, call, patch

import pytest
import requests
from requests import Response, Timeout

from src.apiv5client import ApiV5Client
from src.exceptions import (
    ApiV5BadRequest,
    ApiV5Conflict,
    ApiV5ConnectionError,
    ApiV5Forbidden,
    ApiV5IncorrectMethod,
    ApiV5NoConfig,
    ApiV5NotFound,
    ApiV5RateLimited,
    ApiV5ServerError,
    ApiV5Timeout,
    ApiV5Unauthorized,
)
from tests.fake_resources.fake_response import (
    FakeErrorResponse,
    FakeResponse,
    IterErrorRaiser,
)


@pytest.mark.parametrize(
    "param",
    [
        {"api_base": None},
        {"client_id": None},
        {"client_secret": None},
        {
            "oauth2_token_getter": "something",
            "oauth2_token_setter": None,
        },
    ],
)
def test_api_client_should_raise_error_on_missing_param(param):
    with pytest.raises(ApiV5NoConfig):
        parameters = {
            "api_base": "base_api",
            "client_id": "client_id_123",
            "client_secret": "client_secret_123456",
            "access_token": "token",
        }
        parameters.update(param)
        ApiV5Client(**parameters)


@patch("src.apiv5client.OAuth2Api")
def test_api_client_should_initialize_with_base_parameters(fake_oauth: Mock):
    fake_oauth.return_value = fake_oauth
    fake_oauth.access_token = False

    client = ApiV5Client("base_api", "client_id_123", "client_secret_123456")
    assert client.client_id == "client_id_123"
    assert client.client_secret == "client_secret_123456"
    fake_oauth.assert_has_calls(
        [
            call(
                api_base="base_api",
                client_id="client_id_123",
                client_secret="client_secret_123456",
                timeout=None,
                access_token=None,
                refresh_token=None,
                oauth2_token_getter=None,
                oauth2_token_setter=None,
            )
        ]
    )
    assert client.oauth.get_token.call_count == 1


@patch("src.apiv5client.OAuth2Api")
def test_api_client_should_initialize_with_tokens_and_token_getters(fake_oauth: Mock):
    fake_oauth.return_value = fake_oauth
    fake_oauth.access_token = True

    client = ApiV5Client(
        "base_api",
        "client_id_123",
        "client_secret_123456",
        access_token="access",
        refresh_token="refresh",
        oauth2_token_getter="getter",
        oauth2_token_setter="setter",
    )
    assert client.client_id == "client_id_123"
    assert client.client_secret == "client_secret_123456"
    fake_oauth.assert_has_calls(
        [
            call(
                api_base="base_api",
                client_id="client_id_123",
                client_secret="client_secret_123456",
                timeout=None,
                access_token="access",
                refresh_token="refresh",
                oauth2_token_getter="getter",
                oauth2_token_setter="setter",
            )
        ]
    )
    assert fake_oauth.get_token.call_count == 0


def test_get_header():
    assert ApiV5Client.header() == {"Content-Type": "application/json"}


@patch("src.apiv5client.OAuth2Api")
def test_prepare_request(fake_oauth, api_v5_client: ApiV5Client):
    fake_oauth.return_value = fake_oauth
    fake_oauth.access_token = "my_token"

    url = "/url"
    data = {"aa": 123}
    json = {"bb": 456}
    params = {"cc": 789}
    headers = {"dd": 321}
    url_, headers_, data_, json_, params_ = api_v5_client.prepare_request(
        url, headers, data, json, params, True
    )
    assert url_ == "https://base_api/url"
    assert data_ == data
    assert json_ == json
    assert params_ == params


@pytest.mark.parametrize(
    "method, expected_call",
    [
        (
            "POST",
            call(
                "https://base_api/url",
                headers={"dd": "321"},
                params={"cc": 789},
                data={"aa": 123},
                json={"bb": 456},
                timeout=None,
            ),
        ),
        (
            "GET",
            call(
                "https://base_api/url",
                headers={"dd": "321"},
                params={"cc": 789},
                data={"aa": 123},
                timeout=None,
            ),
        ),
        (
            "PATCH",
            call(
                "https://base_api/url",
                headers={"dd": "321"},
                data={"aa": 123},
                timeout=None,
            ),
        ),
        (
            "PUT",
            call(
                "https://base_api/url",
                headers={"dd": "321"},
                data={"aa": 123},
                timeout=None,
            ),
        ),
        (
            "DELETE",
            call(
                "https://base_api/url",
                headers={"dd": "321"},
                data={"aa": 123},
                timeout=None,
            ),
        ),
    ],
)
@patch("src.apiv5client.OAuth2Api", Mock())
def test_execute_request_should_work(
    method, expected_call: call, api_v5_client: ApiV5Client
):
    url = "https://base_api/url"
    data = {"aa": 123}
    json = {"bb": 456}
    params = {"cc": 789}
    headers = {"dd": "321"}

    with patch("src.apiv5client.requests") as fake_requests:
        http_method = getattr(fake_requests, method.lower())
        http_method.return_value = FakeResponse({"success": "true"})

        result = api_v5_client.execute_request(url, method, headers, data, json, params)

        assert isinstance(result, Response)
        assert result.status_code == 200
        assert result.json() == {"success": "true"}

        assert http_method.call_count == 1
        http_method.assert_has_calls([expected_call])


@pytest.mark.parametrize(
    "status_codes, expected_exception",
    [
        ([404, 410], ApiV5NotFound),
        ([401], ApiV5Unauthorized),
        ([403], ApiV5Forbidden),
        ([409], ApiV5Conflict),
        ([429], ApiV5RateLimited),
        ([400, 402, 444, 499, 501], ApiV5BadRequest),
        ([500, 502, 666], ApiV5ServerError),
    ],
)
@patch("src.apiv5client.OAuth2Api", Mock())
def test_execute_request_should_handle_http_error(
    status_codes, expected_exception, api_v5_client: ApiV5Client
):
    url = "https://base_api/url"
    data = {"aa": 123}
    json = {"bb": 456}
    params = {"cc": 789}
    headers = {"dd": "321"}
    with patch("src.apiv5client.requests") as fake_requests:
        for status_code in status_codes:
            fake_requests.post.return_value = FakeErrorResponse(status_code)
            with pytest.raises(expected_exception):
                api_v5_client.execute_request(url, "POST", headers, data, json, params)


@patch("src.apiv5client.OAuth2Api", Mock())
def test_execute_request_should_raise_error_on_incorrect_http_method(
    api_v5_client: ApiV5Client,
):
    with pytest.raises(ApiV5IncorrectMethod):
        api_v5_client.execute_request(None, "TOTO", None, None, None, None)


@patch("src.apiv5client.OAuth2Api", Mock())
def test_execute_request_should_handle_timeout(api_v5_client: ApiV5Client):
    with patch("src.apiv5client.requests.post") as fake_post:
        fake_post.side_effect = Timeout()
        with pytest.raises(ApiV5Timeout):
            api_v5_client.execute_request(None, "POST", None, None, None, None)


@patch("src.apiv5client.OAuth2Api", Mock())
def test_execute_request_should_handle_connection_error(api_v5_client: ApiV5Client):
    with patch("src.apiv5client.requests.post") as fake_post:
        fake_post.side_effect = requests.exceptions.ConnectionError()

        with pytest.raises(ApiV5ConnectionError):
            api_v5_client.execute_request(None, "POST", None, None, None, None)


@patch("src.apiv5client.OAuth2Api", Mock())
@patch(
    "src.apiv5client.ApiV5Client.execute_request",
    Mock(return_value=FakeResponse({"success": "true"})),
)
@patch(
    "src.apiv5client.ApiV5Client.execute_request",
    Mock(return_value=FakeResponse({"success": "true"})),
)
def test_call_should_work(api_v5_client: ApiV5Client):
    api_v5_client.oauth.access_token = "123"
    url = "/url"
    data = {"aa": 123}
    json = {"bb": 456}
    params = {"cc": 789}
    headers = {"dd": "321"}

    result = api_v5_client.call(url, params, "GET", data, json, headers)

    assert result.status_code == 200
    assert result.json() == {"success": "true"}
    assert api_v5_client.execute_request.call_count == 1
    api_v5_client.execute_request.assert_has_calls(
        [
            call(
                "https://base_api/url",
                "GET",
                {
                    **headers,
                    **{
                        "Content-Type": "application/json",
                        "Authorization": "Bearer 123",
                    },
                },
                data,
                json,
                params,
            )
        ]
    )


def test_call_should_handle_401_with_refresh_token(api_v5_client: ApiV5Client):
    api_v5_client.oauth = Mock()
    with patch("src.apiv5client.requests.get") as fake_get:
        # raise one 401 then 200
        iter_error = IterErrorRaiser(401, max_retry=1)
        fake_get.side_effect = iter_error.get
        api_v5_client.oauth.access_token = 123

        api_v5_client.call("/url", method="GET")

        assert api_v5_client.oauth.refresh_tokens.call_count == 1
        assert api_v5_client.oauth.get_token.call_count == 0
        assert fake_get.call_count == 2


def test_call_should_handle_401_without_refresh_token(api_v5_client: ApiV5Client):
    api_v5_client.oauth = Mock()
    with patch("src.apiv5client.requests.get") as fake_get:
        # raise one 401 then 200
        iter_error = IterErrorRaiser(401, max_retry=1)
        fake_get.side_effect = iter_error.get

        api_v5_client.oauth.access_token = None

        api_v5_client.call("/url", method="GET")

        assert api_v5_client.oauth.refresh_tokens.call_count == 0
        assert api_v5_client.oauth.get_token.call_count == 1
        assert fake_get.call_count == 2


@patch("src.apiv5client.OAuth2Api", Mock())
def test_call_should_let_error_raise(api_v5_client: ApiV5Client):
    with patch(
        "src.apiv5client.requests.get",
        Mock(return_value=FakeErrorResponse(status_code=444)),
    ):
        with pytest.raises(ApiV5BadRequest):
            print(api_v5_client.call("/url", method="GET"))


def test_set_access_token_should_set_token(api_v5_client: ApiV5Client):
    api_v5_client.refresh_token = None
    api_v5_client.oauth.refresh_token = None
    api_v5_client.access_token = None
    api_v5_client.oauth.access_token = None

    token = "super-token"

    api_v5_client.set_access_token(token)

    assert api_v5_client.access_token == token
    assert api_v5_client.oauth.access_token == token
    assert api_v5_client.refresh_token is None
    assert api_v5_client.oauth.refresh_token is None


def test_set_refresh_token_should_set_token(api_v5_client: ApiV5Client):
    api_v5_client.access_token = None
    api_v5_client.oauth.access_token = None
    api_v5_client.refresh_token = None
    api_v5_client.oauth.refresh_token = None

    token = "super-token"

    api_v5_client.set_refresh_token(token)

    assert api_v5_client.refresh_token == token
    assert api_v5_client.oauth.refresh_token == token
    assert api_v5_client.access_token is None
    assert api_v5_client.oauth.access_token is None
