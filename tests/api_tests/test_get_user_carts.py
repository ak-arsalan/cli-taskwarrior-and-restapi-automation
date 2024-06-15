import requests

def test_get_user_carts(base_url):
    user_id = 2
    response = requests.get(f"{base_url}/carts/user/{user_id}")
    assert response.status_code == 200
    carts = response.json()
    for cart in carts:
        assert cart['userId'] == user_id
    print(response.json())
