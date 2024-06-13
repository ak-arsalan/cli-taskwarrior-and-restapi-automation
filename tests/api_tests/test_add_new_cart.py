import requests
import pytest
from config import BASE_URL

def test_add_new_cart():
    new_cart = {
        "userId": 5,
        "date": "2020-02-03",
        "products": [{"productId": 5, "quantity": 1}, {"productId": 1, "quantity": 5}]
    }
    response = requests.post(BASE_URL + "/carts", json=new_cart)
    assert response.status_code == 200
    cart = response.json()
    assert cart['id'] is not None
    assert cart['userId'] == new_cart['userId']
    assert cart['date'] == new_cart['date']
    assert cart['products'] == new_cart['products']
    print(response.json())
