import requests
import pytest
from config import BASE_URL

def test_delete_cart():
    cart_id = 6
    response = requests.delete(f"{BASE_URL}/carts/{cart_id}")
    assert response.status_code == 200
    cart = response.json()
    assert cart['id'] == cart_id
    print(response.json())
