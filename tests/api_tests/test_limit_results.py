import requests
import pytest

BASE_URL = "https://fakestoreapi.com/carts"

def test_limit_results():
    limit = 5
    response = requests.get(f"{BASE_URL}?limit={limit}")
    assert response.status_code == 200
    carts = response.json()
    assert len(carts) == limit
