import uuid
from models.movies_model import Movie as MovieModel
from schemas.movies_schema import MovieCreate, MovieUpdate
from database import Session
from typing import List
from sqlalchemy.orm import joinedload


def create_movie(data: MovieCreate) -> MovieModel:
    db = Session()
    new_movie: MovieModel = MovieModel(**data.dict())
    db.add(new_movie)
    db.commit()
    db.refresh(new_movie)
    # db.close() ERROR: https://docs.sqlalchemy.org/en/20/errors.html#error-bhk3
    return new_movie


def get_movies() -> List[MovieModel]:
    db = Session()
    movies: List[MovieModel] = db.query(MovieModel).options(joinedload(MovieModel.director)).all()
    db.close()
    return movies


def get_movie(id: uuid.UUID) -> MovieModel:
    db = Session()
    movie: MovieModel = db.query(MovieModel).filter(MovieModel.id == id).options(joinedload(MovieModel.director)).first()
    db.close()
    return movie


def update_movie(id: uuid.UUID, data: MovieUpdate) -> MovieModel:
    db = Session()
    movie: MovieModel = db.query(MovieModel).filter(MovieModel.id == id).first()
    movie.title = data.title
    movie.overview = data.overview
    movie.year = data.year
    movie.rating = data.rating
    movie.category = data.category
    db.commit()
    db.refresh(movie)
    # db.close() ERROR: https://docs.sqlalchemy.org/en/20/errors.html#error-bhk3
    return movie


def delete_movie(id: uuid.UUID) -> None:
    db = Session()
    db.query(MovieModel).filter(MovieModel.id == id).delete()
    db.commit()
    db.close()
    return
