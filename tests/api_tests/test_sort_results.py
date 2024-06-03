import requests
import pytest

BASE_URL = "https://fakestoreapi.com/carts"

def test_sort_results():
    response = requests.get(f"{BASE_URL}?sort=desc")
    assert response.status_code == 200
    products = response.json()
    assert products
    product_ids = [product["id"] for product in products]
    assert product_ids == sorted(product_ids, reverse=True)
