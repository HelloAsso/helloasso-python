from helloasso_api import HaApiV5


def test_ha_api_v5_should_instantiate():

    api = HaApiV5("base_url", "client_id", "client_secret", access_token="token")

    assert api.client_id
    assert api.api_base
    assert api.client_secret

    assert api.authorization
