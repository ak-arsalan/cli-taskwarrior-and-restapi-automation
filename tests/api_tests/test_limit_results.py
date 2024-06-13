import requests
import pytest
from config import BASE_URL

def test_limit_results():
    limit = 5
    response = requests.get(f"{BASE_URL}/carts?limit={limit}")
    assert response.status_code == 200
    carts = response.json()
    assert len(carts) == limit
    print(response.json())
