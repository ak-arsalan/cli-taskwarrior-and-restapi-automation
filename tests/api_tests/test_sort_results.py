import requests

def test_sort_results(base_url):
    response = requests.get(f"{base_url}/carts?sort=desc")
    assert response.status_code == 200
    products = response.json()
    assert products
    product_ids = [product["id"] for product in products]
    print("List to String convertion : " , str(product_ids))
    assert product_ids == sorted(product_ids, reverse=True)
    #print(response.json())
