# Movies
REST API for a movies catalog application created with [FastAPI](https://fastapi.tiangolo.com/), [PostgreSQL](https://www.postgresql.org/), [SQLAlchemy](https://www.sqlalchemy.org/), [Alembic](https://alembic.sqlalchemy.org/) and tested with [Pytest](https://docs.pytest.org/en/stable/).
<br>
<br>
It has the following endpoints:

- `POST /api/v1/movies` - Create a new movie

- `GET /api/v1/movies` - Get all movies

- `GET /api/v1/movies/<id>` - Get a specific movie

- `PUT /api/v1/movies/<id>` - Update a whole movie

- `DELETE /api/v1/movies/<id>` - Delete a movie

## Installation
1. Clone the repository
2. Copy `.env.example` to `.env` and fill in the values
3. Run `docker-compose up -d`
4. Run `python3 -m venv venv`
5. Run `source venv/bin/activate`
6. Run `pip3 install -r requirements.txt`
7. Run migrations with `alembic upgrade head`
8. Run ` uvicorn main:app --reload`
9. Go to <a>http://localhost:8000/docs to see the API documentation

## Database migrations
1. Run `alembic revision --autogenerate -m "message"` to autogenerate a new migration file with the changes you made to the models
2. Run `alembic revision -m "message"` to create a new migration file
3. Run `alembic upgrade head` to apply the migrations
4. Run `alembic downgrade -1` to revert the last migration
5. Run `alembic history` to see the migration history
6. Run `alembic current` to see the current migration

## Tests
1. Run `pytest` to run the tests