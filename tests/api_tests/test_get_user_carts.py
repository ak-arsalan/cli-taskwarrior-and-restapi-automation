import requests
import pytest
from config import BASE_URL

def test_get_user_carts():
    user_id = 2
    response = requests.get(f"{BASE_URL}/carts/user/{user_id}")
    assert response.status_code == 200
    carts = response.json()
    for cart in carts:
        assert cart['userId'] == user_id
    print(response.json())
