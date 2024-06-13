import requests
import pytest
from config import BASE_URL

def test_sort_results():
    response = requests.get(f"{BASE_URL}/carts?sort=desc")
    assert response.status_code == 200
    products = response.json()
    assert products
    product_ids = [product["id"] for product in products]
    assert product_ids == sorted(product_ids, reverse=True)
    print(response.json())
