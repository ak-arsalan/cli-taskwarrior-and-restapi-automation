import requests
import pytest

BASE_URL = "https://fakestoreapi.com/carts"

def test_update_cart():
    cart_id = 7
    updated_cart = {
        "userId": 3,
        "date": "2019-12-10",
        "products": [{"productId": 1, "quantity": 3}]
    }
    response = requests.put(f"{BASE_URL}/{cart_id}", json=updated_cart)
    assert response.status_code == 200
    cart = response.json()
    assert cart['id'] == cart_id
    assert cart['userId'] == updated_cart['userId']
    assert cart['date'] == updated_cart['date']
    assert cart['products'] == updated_cart['products']
