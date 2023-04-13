from fastapi.testclient import TestClient
from ..main import app

client = TestClient(app)


def test_server():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == "Movies server running!"


def test_api():
    response = client.get("/api/v1")
    assert response.status_code == 200
    assert response.json() == "Welcome to the movies REST API V1!"
