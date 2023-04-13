from fastapi.testclient import TestClient
from ..main import app
from services import movies_service
from schemas.movies_schema import MovieCreate

client = TestClient(app)


def test_create_movie_successfully():
    response = client.post("/api/v1/movies/", json={
        "title": "Example movie",
        "overview": "Example overview",
        "year": 2023,
        "rating": 9.8,
        "category": "Example category"
    })
    assert response.status_code == 201
    assert response.json().get("title") == "Example movie"
    assert response.json().get("overview") == "Example overview"
    assert response.json().get("year") == 2023
    assert response.json().get("rating") == 9.8
    assert response.json().get("category") == "Example category"
    movies_service.delete_movie(response.json().get("id"))


def test_get_movie_successfully():
    created_movie = movies_service.create_movie(MovieCreate(
        title="Example movie 2",
        overview="Example overview 2",
        year=2023,
        rating=9.8,
        category="Example category 2"
    ))
    response = client.get(f"/api/v1/movies/{created_movie.id}")
    assert response.status_code == 200
    assert response.json() == {
        "id": str(created_movie.id),
        "title": "Example movie 2",
        "overview": "Example overview 2",
        "year": 2023,
        "rating": 9.8,
        "category": "Example category 2"
    }
    movies_service.delete_movie(created_movie.id)


def test_get_movie_not_found():
    response = client.get("/api/v1/movies/00000000-0000-0000-0000-000000000000")
    assert response.status_code == 404
    assert response.json() == {"detail": "Movie not found"}


def test_get_movies_successfully():
    created_movie = movies_service.create_movie(MovieCreate(
        title="Example movie 3",
        overview="Example overview 3",
        year=2023,
        rating=9.8,
        category="Example category 3"
    ))
    response = client.get("/api/v1/movies/")
    assert response.status_code == 200
    assert len(response.json()) >= 1
    assert {
               "id": str(created_movie.id),
               "title": "Example movie 3",
               "overview": "Example overview 3",
               "year": 2023,
               "rating": 9.8,
               "category": "Example category 3"
           } in response.json()
    movies_service.delete_movie(created_movie.id)


def test_update_movie_successfully():
    created_movie = movies_service.create_movie(MovieCreate(
        title="Example movie 4",
        overview="Example overview 4",
        year=2023,
        rating=9.8,
        category="Example category 4"
    ))
    response = client.put(f"/api/v1/movies/{created_movie.id}", json={
        "title": "Example movie 5",
        "overview": "Example overview 5",
        "year": 2023,
        "rating": 9.8,
        "category": "Example category 5"
    })
    assert response.status_code == 200
    assert response.json() == {
        "id": str(created_movie.id),
        "title": "Example movie 5",
        "overview": "Example overview 5",
        "year": 2023,
        "rating": 9.8,
        "category": "Example category 5"
    }
    movies_service.delete_movie(created_movie.id)


def test_update_movie_not_found():
    response = client.put("/api/v1/movies/00000000-0000-0000-0000-000000000000", json={
        "title": "Example movie 6",
        "overview": "Example overview 6",
        "year": 2023,
        "rating": 9.8,
        "category": "Example category 6"
    })
    assert response.status_code == 404
    assert response.json() == {"detail": "Movie not found"}


def test_delete_movie_successfully():
    created_movie = movies_service.create_movie(MovieCreate(
        title="Example movie 7",
        overview="Example overview 7",
        year=2023,
        rating=9.8,
        category="Example category 7"
    ))
    response = client.delete(f"/api/v1/movies/{created_movie.id}")
    assert response.status_code == 204


def test_delete_movie_not_found():
    response = client.delete("/api/v1/movies/00000000-0000-0000-0000-000000000000")
    assert response.status_code == 404
    assert response.json() == {"detail": "Movie not found"}
