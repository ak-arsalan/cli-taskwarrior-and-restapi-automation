import requests
import pytest

BASE_URL = "https://fakestoreapi.com/carts"

def test_get_all_carts():
    response = requests.get(BASE_URL)
    assert response.status_code == 200
    carts = response.json()
    assert isinstance(carts, list)
    assert len(carts) > 0