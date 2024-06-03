import requests
import pytest

BASE_URL = "https://fakestoreapi.com/carts"

def test_get_user_carts():
    user_id = 2
    response = requests.get(f"{BASE_URL}/user/{user_id}")
    assert response.status_code == 200
    carts = response.json()
    for cart in carts:
        assert cart['userId'] == user_id
