import requests
import pytest

BASE_URL = "https://fakestoreapi.com/carts"

def test_get_single_cart():
    cart_id = 5
    response = requests.get(f"{BASE_URL}/{cart_id}")
    assert response.status_code == 200
    cart = response.json()
    assert cart['id'] == cart_id
    assert 'userId' in cart
    assert 'date' in cart
    assert 'products' in cart
