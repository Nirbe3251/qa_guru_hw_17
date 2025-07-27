from http.client import responses

import requests

url = "https://reqres.in/"
endpoint = '/api/users'
register_endpoint = '/api/register'
login_endpoint = '/api/login'

def test_list_users():
    response = requests.get(url + endpoint, params={'page': 2})
    body = response.json()

    assert response.status_code == 200
    assert body['page'] == 2


def test_single_user():
    single_user_endpoint = '/2'

    response = requests.get(url + endpoint + single_user_endpoint)
    body = response.json()

    assert response.status_code == 200
    assert body['data']["id"] == 2

def test_single_user_not_found():
    single_user_endpoint = '/23'
    headers = {
        'x-api-key': 'reqres-free-v1'
    }
    response = requests.get(url + endpoint + single_user_endpoint, headers=headers)
    body = response.json()

    assert response.status_code == 404

def test_create_user():
    name = 'daniil'
    job = 'qa'

    payload = {
        'name': name,
        'job': job
    }

    headers = {
        'x-api-key': 'reqres-free-v1'
    }

    response = requests.post(url + endpoint, json=payload, headers=headers)

    assert response.status_code == 201

def test_update_user():
    name = 'daniil'
    job = 'qa'
    id = '/2'

    payload = {
        'name': name,
        'job': job
    }

    headers = {
        'x-api-key': 'reqres-free-v1'
    }

    response = requests.put(url + endpoint + id, json=payload, headers=headers)

    assert response.status_code == 200

def test_delete_user():
    id = '/2'

    headers = {
        'x-api-key': 'reqres-free-v1'
    }

    response = requests.delete(url + endpoint + id, headers=headers)

    assert response.status_code == 204

def test_register_success():
    email = 'eve.holt@reqres.in'
    password = 'pistol'

    payload = {
        'email': email,
        'password': password
    }

    headers = {
        'x-api-key': 'reqres-free-v1'
    }

    response = requests.post(url + register_endpoint, json=payload, headers=headers)
    body = response.json()

    assert response.status_code == 200

def test_register_unsuccess():
    email = 'eve.holt@reqres.in'

    payload = {
        'email': email,
    }

    headers = {
        'x-api-key': 'reqres-free-v1'
    }

    response = requests.post(url + register_endpoint, json=payload, headers=headers)
    body = response.json()

    assert response.status_code == 400

def test_login_success():
    email = 'eve.holt@reqres.in'
    password = 'pistol'

    payload = {
        'email': email,
        'password': password
    }

    headers = {
        'x-api-key': 'reqres-free-v1'
    }

    response = requests.post(url + register_endpoint, json=payload, headers=headers)

    assert response.status_code == 200


def test_login_unsuccess():
    email = 'eve.holt@reqres.in'

    payload = {
        'email': email,
    }

    headers = {
        'x-api-key': 'reqres-free-v1'
    }

    response = requests.post(url + register_endpoint, json=payload, headers=headers)

    assert response.status_code == 400