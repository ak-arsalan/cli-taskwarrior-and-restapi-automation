import requests

def test_get_carts_in_date_range(base_url):
    start_date = "2019-12-10"
    end_date = "2020-10-10"
    response = requests.get(f"{base_url}/carts?startdate={start_date}&enddate={end_date}")
    assert response.status_code == 200
    carts = response.json()
    for cart in carts:
        assert start_date <= cart['date'] <= end_date
    print(response.json())
