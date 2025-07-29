import requests
from jsonschema import validate

import schemas

url = "https://reqres.in/"
list_user_endpoint = '/api/users'
endpoint = '/api/users/'
register_endpoint = '/api/register'
login_endpoint = '/api/login'

def test_list_users():
    response = requests.get(url + list_user_endpoint, params={'page': 2})
    body = response.json()

    assert response.status_code == 200
    assert body['page'] == 2


def test_get_single_user():
    user_id = '2'
    headers = {
        'x-api-key': 'reqres-free-v1'
    }
    response = requests.get(url + endpoint + user_id, headers=headers)
    body = response.json()

    assert response.status_code == 200
    assert body["data"]["email"] == "janet.weaver@reqres.in"
    assert body["data"]["first_name"] == "Janet"
    assert body["data"]["last_name"] == "Weaver"

    validate(body, schema=schemas.get_single_user)

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
    validate(response.json(), schema=schemas.create_user)

def test_update_user():
    name = 'daniil'
    job = 'qa'
    id = '2'

    payload = {
        'name': name,
        'job': job
    }

    headers = {
        'x-api-key': 'reqres-free-v1'
    }

    response = requests.put(url + endpoint + id, json=payload, headers=headers)

    assert response.status_code == 200
    validate(response.json(), schema=schemas.update_user)


def test_delete_user():
    id = '2'

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

    assert response.status_code == 200
    validate(response.json(), schema=schemas.register_user)

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
    validate(response.json(), schema=schemas.register_unsuccessful)

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

def test_login_with_negative_email():
    email = 'eve.holtreqres.in'
    password = 'pistol'

    payload = {
        'email': email,
        'password': password
    }

    headers = {
        'x-api-key': 'reqres-free-v1'
    }

    response = requests.post(url + register_endpoint, json=payload, headers=headers)

    assert response.status_code == 400