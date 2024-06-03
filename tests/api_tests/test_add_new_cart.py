import requests
import pytest

BASE_URL = "https://fakestoreapi.com/carts"

def test_add_new_cart():
    new_cart = {
        "userId": 5,
        "date": "2020-02-03",
        "products": [{"productId": 5, "quantity": 1}, {"productId": 1, "quantity": 5}]
    }
    response = requests.post(BASE_URL, json=new_cart)
    assert response.status_code == 200
    cart = response.json()
    assert cart['id'] is not None
    assert cart['userId'] == new_cart['userId']
    assert cart['date'] == new_cart['date']
    assert cart['products'] == new_cart['products']
