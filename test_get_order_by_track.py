# Ленин Сергей, 46-я когорта — Финальный проект. Инженер по тестированию плюс

import configuration

import requests

import data

import post_order

def test_positive_assert():

    track = post_order.get_order_track()
    
    response = post_order.get_order_by_track(track)
    
    assert response.status_code == 200