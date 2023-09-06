from fastapi.testclient import TestClient
from ..main import app
from services import movies_service, users_service, directors_service
from schemas.movies_schema import MovieCreate
from schemas.directors_schema import DirectorCreate, Director

client = TestClient(app)

data = {
    "full_name": "Example Test Movies",
    "email": "example.test.movie@gmail.com",
    "password": "example_password",
}


def create_needed_data():
    user = client.post("/api/v1/auth/register", json=data)
    user = user.json()
    token = user.get("token")
    director_data = directors_service.create_director(DirectorCreate(full_name="Example Movies Director"))
    director = Director.from_orm(director_data).dict()
    return user, token, director


user, token, director = create_needed_data()


def test_create_movie_successfully():
    response = client.post("/api/v1/movies/", json={
        "title": "Example movie",
        "overview": "Example overview",
        "year": 2023,
        "rating": 9.8,
        "category": "Example category",
        "director_id": str(director.get("id"))
    }, headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 201
    assert response.json().get("title") == "Example movie"
    assert response.json().get("overview") == "Example overview"
    assert response.json().get("year") == 2023
    assert response.json().get("rating") == 9.8
    assert response.json().get("category") == "Example category"
    assert response.json().get("director_id") == str(director.get("id"))
    movies_service.delete_movie(response.json().get("id"))


def test_get_movie_successfully():
    created_movie = movies_service.create_movie(MovieCreate(
        title="Example movie 2",
        overview="Example overview 2",
        year=2023,
        rating=9.8,
        category="Example category 2",
        director_id=str(director.get("id"))
    ))
    print(created_movie.id)
    response = client.get(f"/api/v1/movies/{created_movie.id}", headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200
    assert response.json() == {
        "id": str(created_movie.id),
        "title": "Example movie 2",
        "overview": "Example overview 2",
        "year": 2023,
        "rating": 9.8,
        "category": "Example category 2",
        "director_id": str(director.get("id")),
        "director": {
            "id": str(director.get("id")),
            "full_name": "Example Movies Director"
        }
    }
    movies_service.delete_movie(created_movie.id)


def test_get_movie_not_found():
    response = client.get(
        "/api/v1/movies/00000000-0000-0000-0000-000000000000",
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 404
    assert response.json() == {"detail": "Movie not found"}


def test_get_movies_successfully():
    created_movie = movies_service.create_movie(MovieCreate(
        title="Example movie 3",
        overview="Example overview 3",
        year=2023,
        rating=9.8,
        category="Example category 3",
        director_id=str(director.get("id"))
    ))
    response = client.get("/api/v1/movies/", headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200
    assert len(response.json()) >= 1
    assert {
               "id": str(created_movie.id),
               "title": "Example movie 3",
               "overview": "Example overview 3",
               "year": 2023,
               "rating": 9.8,
               "category": "Example category 3",
               "director_id": str(director.get("id")),
               "director": {
                  "id": str(director.get("id")),
                  "full_name": "Example Movies Director"
               }
           } in response.json()
    movies_service.delete_movie(created_movie.id)


def test_update_movie_successfully():
    created_movie = movies_service.create_movie(MovieCreate(
        title="Example movie 4",
        overview="Example overview 4",
        year=2023,
        rating=9.8,
        category="Example category 4",
        director_id=str(director.get("id"))
    ))
    response = client.put(f"/api/v1/movies/{created_movie.id}", json={
        "title": "Example movie 5",
        "overview": "Example overview 5",
        "year": 2023,
        "rating": 9.8,
        "category": "Example category 5",
        "director_id": str(director.get("id"))
    }, headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200
    assert response.json() == {
        "id": str(created_movie.id),
        "title": "Example movie 5",
        "overview": "Example overview 5",
        "year": 2023,
        "rating": 9.8,
        "category": "Example category 5",
        "director_id": str(director.get("id")),
        "director": {
            "id": str(director.get("id")),
            "full_name": "Example Movies Director"
        }
    }
    movies_service.delete_movie(created_movie.id)


def test_update_movie_not_found():
    response = client.put("/api/v1/movies/00000000-0000-0000-0000-000000000000", json={
        "title": "Example movie 6",
        "overview": "Example overview 6",
        "year": 2023,
        "rating": 9.8,
        "category": "Example category 6",
        "director_id": str(director.get("id"))
    }, headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 404
    assert response.json() == {"detail": "Movie not found"}


def test_delete_movie_successfully():
    created_movie = movies_service.create_movie(MovieCreate(
        title="Example movie 7",
        overview="Example overview 7",
        year=2023,
        rating=9.8,
        category="Example category 7",
        director_id=str(director.get("id"))
    ))
    response = client.delete(
        f"/api/v1/movies/{created_movie.id}",
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 204


def test_delete_movie_not_found():
    response = client.delete(
        "/api/v1/movies/00000000-0000-0000-0000-000000000000",
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 404
    assert response.json() == {"detail": "Movie not found"}


def test_delete_needed_data():
    directors_service.delete_director(director.get("id"))
    users_service.delete_user(user.get("id"))
    assert True
