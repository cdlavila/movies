from fastapi.testclient import TestClient
from ..main import app
from services import users_service
from schemas.auth_schema import AuthRegister

client = TestClient(app)

data = {
    "full_name": "Example Test User",
    "email": "example.test.user@gmail.com",
    "password": "example_password",
}


def test_get_myself_successfully():
    register_response = client.post("/api/v1/auth/register", json=data)
    token = register_response.json().get("token")
    response = client.get("/api/v1/users/me", headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200
    assert response.json().get("id") == register_response.json().get("id")
    assert response.json().get("full_name") == data.get("full_name")
    assert response.json().get("email") == data.get("email")
    users_service.delete_user(response.json().get("id"))
