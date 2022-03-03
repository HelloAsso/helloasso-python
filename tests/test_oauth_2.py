from logging import Logger
from unittest.mock import Mock, call, patch

import pytest
import requests
from oauthlib.oauth2 import (
    AccessDeniedError,
    BackendApplicationClient,
    UnauthorizedClientError,
)
from requests.auth import HTTPBasicAuth

from helloasso_apiv5.exceptions import (
    ApiV5AuthenticationError,
    ApiV5ConnectionError,
    Apiv5ExceptionError,
    ApiV5Timeout,
)
from helloasso_apiv5.oauth2 import OAuth2Api


def get_oauth():
    return OAuth2Api("base_api", "client_id_123", "client_secret_123456", 123)


def test_oauth2_should_initialize():
    oauth = get_oauth()
    assert oauth.client_id == "client_id_123"
    assert oauth.client_secret == "client_secret_123456"
    assert oauth.timeout == 123
    assert oauth._access_token is None
    assert oauth._refresh_token is None
    assert oauth.oauth2_token_getter is None
    assert oauth.oauth2_token_setter is None
    assert isinstance(oauth.client, BackendApplicationClient)
    assert isinstance(oauth.auth, HTTPBasicAuth)
    assert isinstance(oauth.log, Logger)


def test_oauth2_should_initialize_with_optional_params():
    oauth = OAuth2Api(
        "api_base",
        "client_id_123",
        "client_secret_123456",
        None,
        access_token="access_token",
        refresh_token="refresh_token",
        oauth2_token_getter="getter",
        oauth2_token_setter="setter",
    )
    assert oauth.client_id == "client_id_123"
    assert oauth.client_secret == "client_secret_123456"
    assert oauth.timeout is None
    assert oauth._access_token == "access_token"
    assert oauth._refresh_token == "refresh_token"
    assert oauth.oauth2_token_getter == "getter"
    assert oauth.oauth2_token_setter == "setter"
    assert isinstance(oauth.client, BackendApplicationClient)
    assert isinstance(oauth.auth, HTTPBasicAuth)
    assert isinstance(oauth.log, Logger)


def test_get_path_should_work():
    oauth = get_oauth()
    assert oauth._get_path() == "https://base_api/oauth2/token"


def test_get_headers():
    oauth = get_oauth()
    assert oauth._get_headers() == {
        "cache-control": "no-cache",
        "content-type": "application/x-www-form-urlencoded",
    }


def test_access_token_getter_should_work():
    oauth = get_oauth()
    assert oauth._access_token is None
    assert oauth.access_token is None
    oauth.access_token = 123
    assert oauth.access_token == 123
    oauth.oauth2_token_getter = Mock()
    print(oauth.access_token)
    oauth.oauth2_token_getter.assert_has_calls([call("access_token", "client_id_123")])


def test_access_token_setter_should_work():
    oauth = get_oauth()
    assert oauth._access_token is None
    oauth.access_token = 123
    assert oauth._access_token == 123
    oauth.oauth2_token_setter = Mock()
    oauth.access_token = 123
    oauth.oauth2_token_setter.assert_has_calls(
        [call("access_token", "client_id_123", 123)]
    )


def test_refresh_token_getter_should_work():
    oauth = get_oauth()
    assert oauth._refresh_token is None
    assert oauth.refresh_token is None
    oauth.refresh_token = 123
    assert oauth.refresh_token == 123
    oauth.oauth2_token_getter = Mock()
    print(oauth.refresh_token)
    oauth.oauth2_token_getter.assert_has_calls([call("refresh_token", "client_id_123")])


def test_refresh_token_setter_should_work():
    oauth = get_oauth()
    assert oauth._refresh_token is None
    oauth.refresh_token = 123
    assert oauth.refresh_token == 123
    oauth.oauth2_token_setter = Mock()
    oauth.refresh_token = 123
    oauth.oauth2_token_setter.assert_has_calls(
        [call("refresh_token", "client_id_123", 123)]
    )


def test_credentials_should_work():
    assert get_oauth().credentials == {
        "client_id": "client_id_123",
        "client_secret": "client_secret_123456",
        "refresh_token": None,
    }


@patch("helloasso_apiv5.oauth2.OAuth2Api.token_saver")
@patch("helloasso_apiv5.oauth2.OAuth2Session")
def test_get_token_should_work(OAuth2Session, fake_token_saver):
    OAuth2Session.return_value = OAuth2Session
    oauth = get_oauth()
    oauth.auth = "AUTH OBJECT"
    OAuth2Session.fetch_token.return_value = "fetch_token_return_value"

    oauth.get_token()

    assert OAuth2Session.fetch_token.call_count == 1
    OAuth2Session.fetch_token.assert_has_calls(
        [
            call(
                token_url="https://base_api/oauth2/token",
                auth="AUTH OBJECT",
                timeout=123,
            )
        ]
    )

    assert fake_token_saver.call_count == 1
    fake_token_saver.assert_has_calls([call("fetch_token_return_value")])


@pytest.mark.parametrize(
    "initial_exception, expected_exception",
    [
        (requests.exceptions.ConnectionError, ApiV5ConnectionError),
        (requests.exceptions.Timeout, ApiV5Timeout),
        (UnauthorizedClientError, ApiV5AuthenticationError),
        (Exception, Apiv5ExceptionError),
    ],
)
def test_get_token_should_map_exception(initial_exception, expected_exception):
    with patch("helloasso_apiv5.oauth2.OAuth2Session") as OAuth2Session:
        OAuth2Session.fetch_token.side_effect = initial_exception()
        OAuth2Session.return_value = OAuth2Session
        oauth = get_oauth()
        with pytest.raises(expected_exception):
            oauth.get_token()


def test_token_saver_should_work():
    oauth = get_oauth()
    oauth.token_saver(
        {
            "access_token": 123,
            "refresh_token": 456,
        }
    )
    assert oauth._access_token == 123
    assert oauth._refresh_token == 456


@patch("helloasso_apiv5.oauth2.OAuth2Api.token_saver")
@patch("helloasso_apiv5.oauth2.OAuth2Session")
@patch("helloasso_apiv5.oauth2.OAuth2Api.credentials", {"a": 1})
@patch("helloasso_apiv5.oauth2.OAuth2Api.get_token", Mock())
def test_refresh_tokens_should_work_when_auth_token_is_set(
    OAuth2Session, fake_token_saver
):
    OAuth2Session.return_value = OAuth2Session
    oauth = get_oauth()
    oauth.refresh_token = 123
    OAuth2Session.refresh_token.return_value = "fetch_token_return_value"
    oauth.refresh_tokens()
    assert OAuth2Session.refresh_token.call_count == 1
    OAuth2Session.refresh_token.assert_has_calls(
        [call(token_url="https://base_api/oauth2/token", timeout=123, a=1)]
    )
    assert oauth.get_token.call_count == 1


@patch("helloasso_apiv5.oauth2.OAuth2Api.get_token")
@patch("helloasso_apiv5.oauth2.OAuth2Session")
def test_refresh_tokens_should_work_when_auth_token_is_not_set(
    OAuth2Session, fake_get_token
):
    OAuth2Session.return_value = OAuth2Session
    oauth = get_oauth()
    oauth.access_token = 123
    oauth.refresh_tokens()
    assert OAuth2Session.refresh_token.call_count == 0
    assert oauth.access_token is None
    assert oauth.refresh_token is None
    assert fake_get_token.call_count == 1


@pytest.mark.parametrize(
    "initial_exception, expected_exception",
    [
        (requests.exceptions.ConnectionError, ApiV5ConnectionError),
        (requests.exceptions.Timeout, ApiV5Timeout),
        (UnauthorizedClientError, ApiV5AuthenticationError),
        (Exception, Apiv5ExceptionError),
    ],
)
def test_refresh_tokens_should_map_exception(initial_exception, expected_exception):
    with patch("helloasso_apiv5.oauth2.OAuth2Session") as OAuth2Session:
        OAuth2Session.refresh_token.side_effect = initial_exception()
        OAuth2Session.return_value = OAuth2Session
        oauth = get_oauth()
        oauth.refresh_token = 123
        with pytest.raises(expected_exception):
            oauth.refresh_tokens()


@patch("helloasso_apiv5.oauth2.OAuth2Api.get_token")
def test_refresh_tokens_should_handle_access_denied_error(fake_get_token):
    with patch("helloasso_apiv5.oauth2.OAuth2Session") as OAuth2Session:
        OAuth2Session.refresh_token.side_effect = AccessDeniedError()
        OAuth2Session.return_value = OAuth2Session
        oauth = get_oauth()
        oauth.refresh_token = 123
        oauth.refresh_tokens()
        assert oauth.access_token is None
        assert oauth.refresh_token is None
        assert fake_get_token.call_count == 1
