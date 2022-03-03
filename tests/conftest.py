import pytest

from src import ApiV5Client, HaApiV5


@pytest.fixture
def ha_api_v5_client() -> HaApiV5:
    """Return an ApiV5 Client."""
    return HaApiV5(
        api_base="api.base_api",
        client_id="client_id_123",
        client_secret="client_secret_123456",
        access_token="token",
    )


@pytest.fixture
def api_v5_client() -> ApiV5Client:
    return ApiV5Client(
        api_base="base_api",
        client_id="client_id_123",
        client_secret="client_secret_123456",
        access_token="token",
    )
