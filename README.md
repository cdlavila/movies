# Movies
REST API for a movies catalog application created with [FastAPI](https://fastapi.tiangolo.com/), [PostgreSQL](https://www.postgresql.org/) and [SQLAlchemy](https://www.sqlalchemy.org/).
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
4. Run `pip3 install -r requirements.txt`
5. Run ` uvicorn main:app --reload`
6. Go to <a>http://localhost:8000/docs to see the API documentation
