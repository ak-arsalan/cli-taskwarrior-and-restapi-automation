import requests

def test_get_single_cart(base_url):
    cart_id = 5
    response = requests.get(f"{base_url}/carts/{cart_id}")
    assert response.status_code == 200
    cart = response.json()
    assert cart['id'] == cart_id
    assert 'userId' in cart
    assert 'date' in cart
    assert 'products' in cart
    print(response.json())
