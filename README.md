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
3. Run `docker-compose up -d postgres`
4. Run `python3 -m venv venv`
5. Run `source venv/bin/activate`
6. Run `pip3 install -r requirements.txt`
7. Run migrations with `alembic upgrade head`
8. Run `python -m uvicorn main:app --reload` or `uvicorn main:app --host 0.0.0.0 --port 8000` to start the server
9. OPTIONAL: Run `pm2 start "/home/ubuntu/movies/venv/bin/uvicorn main:app --port 8000 --host 0.0.0.0" --name "movies"` to start the server with pm2
10. Go to <a>http://localhost:8000/docs to see the API documentation

## Database migrations
1. Run `alembic revision --autogenerate -m "message"` to autogenerate a new migration file with the changes you made to the models
2. Run `alembic revision -m "message"` to create a new migration file
3. Run `alembic upgrade head` to apply the migrations
4. Run `alembic downgrade -1` to revert the last migration
5. Run `alembic downgrade base` to revert all migrations
6. Run `alembic downgrade <migration_name>` to revert to a specific migration
7. Run `alembic downgrade <number>` to revert a specific migration and all the migrations after it
8. Run `alembic history` to see the migration history
9. Run `alembic current` to see the current migration

## Tests
1. Run `pytest` to run the tests
2. Run `pytest filename.py` to run the tests in a specific file

## Linter
1. Run `pylint filename.py` to run the linter on a specific file
2. Run `pylint foldername` to run the linter on a specific folder

## Docker
Additionally, if you want to run the application with docker, you can do it with the following command:
```bash
docker-compose up -d app
```
Make sure you have followed the previos steps of the installation process.

You can test the application by going to <a>http://localhost:8000/docs </a>