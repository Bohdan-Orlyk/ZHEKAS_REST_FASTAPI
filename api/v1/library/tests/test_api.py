from base64 import b64encode
from sqlmodel import Session
from fastapi.testclient import TestClient
from conftest import client_fixture, session_fixture, create_test_user_in_db


def test_register_user(client: TestClient):
    user_data = {
        "name": "Test",
        "surname": "User",
        "email": "user@example.com",
        "password": "qwerty12345"
    }

    response = client.post("/users/register/", json=user_data)

    response_data = response.json()

    assert response.status_code == 201
    assert response_data["id"] is not None
    assert response_data["name"] == "Test"


def test_get_users(client: TestClient, session: Session):
    create_test_user_in_db(session=session)

    response = client.get("/users/")

    response_data = response.json()

    assert response.status_code == 200
    assert len(response_data) != 0


def test_login_existing_user(client: TestClient, session: Session):
    test_user = create_test_user_in_db(session=session)

    auth_string = f"{test_user.email}:{test_user.password}"
    auth_header_str = "Basic " + b64encode(auth_string.encode()).decode()
    auth_header = {"Authorization": f'{auth_header_str}'}

    response = client.post("/users/login/", headers={**auth_header})
    response_data = response.json()

    assert response_data["code"] == 200
    assert response_data["login"] == "OK"


def test_get_empty_articles(client: TestClient):
    response = client.get(url="/articles/")
    print(response.json())

    assert response.status_code == 200
    assert response.json() == []


def test_create_article(client: TestClient, session: Session):
    test_user = create_test_user_in_db(session=session)

    auth_string = f"{test_user.email}:{test_user.password}"
    auth_header_str = "Basic " + b64encode(auth_string.encode()).decode()
    auth_header = {"Authorization": f'{auth_header_str}'}

    article = {
        "name": "TEST name",
        "content": "Test CONTENT"
    }
    response = client.post("/articles/", headers={**auth_header}, json=article)
    response_data = response.json()

    assert response.status_code == 201

    assert response_data["name"] == "TEST name"
    assert response_data["content"] == "Test CONTENT"
    assert response_data["id"] != 0
    assert response_data["user_id"] != 0

