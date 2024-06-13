import requests
import pytest
from config import BASE_URL

def test_get_all_carts():
    response = requests.get(BASE_URL+"/carts")
    assert response.status_code == 200
    carts = response.json()
    assert isinstance(carts, list)
    assert len(carts) > 0
    print(response.json())