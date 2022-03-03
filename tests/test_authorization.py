from unittest.mock import Mock, call, patch
from urllib.parse import urlparse

import pytest

from helloasso_api import HaApiV5
from helloasso_api.exceptions import Apiv5ValueError
from tests.fake_resources.fake_response import FakeResponse


def test_authorization_generate_authorize_request(ha_api_v5_client: HaApiV5):
    request = ha_api_v5_client.authorization.generate_authorize_request("redirect", "123")

    assert request["url"] == "https://auth.base_auth/authorize"
    url = urlparse(request["full_url"])
    assert all([url.scheme, url.netloc])
    full_url = urlparse(request["full_url"])
    assert all([full_url.scheme, full_url.netloc])

    assert type(request["code_verifier"]) is str
    assert len(request["code_verifier"]) > 10
    assert type(request["full_url"]) is str
    assert len(request["full_url"]) > 10

    assert request["params"]["client_id"] == ha_api_v5_client.client_id
    assert request["params"]["redirect_uri"] == "redirect"
    assert type(request["params"]["code_challenge"]) is str
    assert len(request["params"]["code_challenge"]) > 10
    assert request["params"]["code_challenge_method"] == "S256"
    assert request["params"]["state"] == "123"


@pytest.mark.parametrize("state", ["a" * 501, {}, 123, None])
def test_authorization_generate_authorize_request_should_raise_exception_on_incorrect_state(
    state, ha_api_v5_client: HaApiV5
):
    with pytest.raises(Apiv5ValueError):
        ha_api_v5_client.authorization.generate_authorize_request("redirect", state)


@patch("helloasso_api.apiv5client.ApiV5Client.call")
def test_authorization_exchange_authorization_token(
    fake_call: Mock, ha_api_v5_client: HaApiV5
):
    fake_response = {
        "access_token": "access_token",
        "refresh_token": "refresh_token",
        "token_type": "token_type",
        "expires_in": "expires_in",
        "organization_slug": "organization_slug",
    }
    fake_call.return_value = FakeResponse(fake_response)

    response = ha_api_v5_client.authorization.exchange_authorization_token(
        "123456", "redirect", "abcd"
    )

    assert response == fake_response

    assert fake_call.call_count == 1
    fake_call.assert_has_calls(
        [
            call(
                "/oauth2/token",
                method="POST",
                data={
                    "client_id": "client_id_123",
                    "client_secret": "client_secret_123456",
                    "grant_type": "authorization_code",
                    "code": "123456",
                    "redirect_uri": "redirect",
                    "code_verifier": "abcd",
                },
                headers={"content-type": "application/x-www-form-urlencoded"},
                include_auth=False,
            )
        ]
    )
