import requests
import pytest

BASE_URL = "https://fakestoreapi.com/carts"

def test_delete_cart():
    cart_id = 6
    response = requests.delete(f"{BASE_URL}/{cart_id}")
    assert response.status_code == 200
    cart = response.json()
    assert cart['id'] == cart_id
