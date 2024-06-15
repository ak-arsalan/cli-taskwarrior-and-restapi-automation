import requests

def test_get_all_carts(base_url):
    response = requests.get(base_url + "/carts")
    assert response.status_code == 200
    carts = response.json()
    assert isinstance(carts, list)
    assert len(carts) > 0
    print(response.json())