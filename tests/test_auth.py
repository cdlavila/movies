from fastapi.testclient import TestClient
from ..main import app
from services import auth_service, users_service
from schemas.auth_schema import AuthRegister

client = TestClient(app)

data = {
    "full_name": "Example Test Auth",
    "email": "example.test.auth@gmail.com",
    "password": "example_password",
}


def test_register_user_successfully():
    response = client.post("/api/v1/auth/register", json=data)
    assert response.status_code == 201
    assert response.json().get("id") is not None
    assert response.json().get("full_name") == data.get("full_name")
    assert response.json().get("email") == data.get("email")
    assert response.json().get("token") is not None
    users_service.delete_user(response.json().get("id"))


def test_login_user_successfully():
    auth_service.register(AuthRegister(**data))
    response = client.post("/api/v1/auth/login", json={
        "email": data.get("email"),
        "password": data.get("password"),
    })
    assert response.status_code == 200
    assert response.json().get("id") is not None
    assert response.json().get("full_name") == data.get("full_name")
    assert response.json().get("email") == data.get("email")
    assert response.json().get("token") is not None
    users_service.delete_user(response.json().get("id"))
