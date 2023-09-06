from fastapi.testclient import TestClient
from ..main import app
from schemas.directors_schema import Director
from services import directors_service, users_service

client = TestClient(app)

data = {
    "full_name": "Example Test Director",
    "email": "example.test.director@gmail.com",
    "password": "example_password",
}


def test_create_director_successfully():
    register_response = client.post("/api/v1/auth/register", json=data)
    token = register_response.json().get("token")
    response = client.post("/api/v1/directors/", json={
        "full_name": data.get("full_name"),
    }, headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 201
    assert response.json().get("id") is not None
    assert response.json().get("full_name") == data.get("full_name")
    users_service.delete_user(register_response.json().get("id"))
    directors_service.delete_director(response.json().get("id"))


def test_get_directors_successfully():
    register_response = client.post("/api/v1/auth/register", json=data)
    token = register_response.json().get("token")
    created_director = directors_service.create_director(Director(full_name=data.get("full_name")))
    response = client.get("/api/v1/directors/", headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200
    assert len(response.json()) >= 1
    assert {
        "id": str(created_director.id),
        "full_name": data.get("full_name"),
    } in response.json()
    users_service.delete_user(register_response.json().get("id"))
    directors_service.delete_director(created_director.id)
