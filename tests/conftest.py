import pytest
import requests

@pytest.fixture
def base_url():
    return "https://dog.ceo/api"

@pytest.fixture
def get_response():
    def _get_response(endpoint):
        url = f"https://dog.ceo/api{endpoint}"
        return requests.get(url)
    return _get_response