import requests

def test_view_all_products(base_url):
    add_new_product = {
        "title": 'test product',
        "price": 13.5,
        "description": 'lorem ipsum set',
        "image": 'https://i.pravatar.cc',
        "category": 'electronic'
    }

    response = requests.post(base_url + "/products" , add_new_product)
    added_product = response.json()
    assert added_product["title"] == "test product"
    assert add_new_product["title"]  == "test product"
    assert response.status_code == 200
    print(response.json())
