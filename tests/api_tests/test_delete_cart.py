import requests

def test_delete_cart(base_url):
    cart_id = 6
    response = requests.delete(f"{base_url}/carts/{cart_id}")
    assert response.status_code == 200
    cart = response.json()
    assert cart['id'] == cart_id
    print(response.json())
