import requests

def test_limit_results(base_url):
    limit = 5
    response = requests.get(f"{base_url}/carts?limit={limit}")
    assert response.status_code == 200
    carts = response.json()
    assert len(carts) == limit
    print(response.json())
