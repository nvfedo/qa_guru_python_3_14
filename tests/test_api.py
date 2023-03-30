import requests
from pytest_voluptuous import S
from requests import Response
import schema.schema


def test_create_user():
    create_user: Response = requests.post(
        url="https://reqres.in/api/users",
        json=
        {
            "name": "Nikita",
            "job": "Quality Assurance"
        }
    )
    assert create_user.status_code == 201
    assert create_user.json()["name"] == "Nikita"
    assert create_user.json()["job"] == "Quality Assurance"
    assert create_user.json()["createdAt"] is not None
    assert create_user.json()["id"] is not None
    assert S(schema.schema.create_user) == create_user.json()


def test_update_user():
    update_user: Response = requests.put(
        url="https://reqres.in/api/users/2",
        json=
        {
            "name": "Nikita Fedotov",
            "job": "Quality Control"
        }
    )
    assert update_user.status_code == 200
    assert update_user.json()["name"] == "Nikita Fedotov"
    assert update_user.json()["job"] == "Quality Control"
    assert update_user.json()["updatedAt"] is not None
    assert S(schema.schema.update_user) == update_user.json()


def test_delete_user():
    delete_user: Response = requests.delete(url=" https://reqres.in/api/users/2")
    assert delete_user.status_code == 204


def test_login_successfully():
    login_successfully: Response = requests.post(
        url="https://reqres.in/api/login",
        json=
        {
            "email": "eve.holt@reqres.in",
            "password": "cityslicka"
        }
    )
    assert login_successfully.status_code == 200
    assert login_successfully.json()["token"] == "QpwL5tke4Pnpja7X4"
    assert S(schema.schema.login_successfully) == login_successfully.json()


def test_login_unsuccessfully():
    login_unsuccessfully: Response = requests.post(
        url="https://reqres.in/api/login",
        json=
        {
            "email": "wrong@email",
        }
    )

    assert login_unsuccessfully.status_code == 400
    assert S(schema.schema.login_unsuccessfully) == login_unsuccessfully.json()
