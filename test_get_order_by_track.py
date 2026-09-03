import configuration

import requests

import data

def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDERS,
                         json=body,
                         headers=data.headers)

def get_order_track():

    response = post_new_order(data.order_body)

    return response.json()["track"]

def get_order_by_track(track):
    params = {"t": track}
    response = requests.get(
        configuration.URL_SERVICE + configuration.GET_ORDERS_TRACK,
        params=params
    )
    return response

def test_positive_assert():

    track = get_order_track()
    
    response = get_order_by_track(track)
    
    assert response.status_code == 200
    



