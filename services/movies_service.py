import uuid
from models.movies_model import Movie as MovieModel
from schemas.movies_schema import MovieCreate, MovieUpdate
from database import Session


def create_movie(data: MovieCreate):
    db = Session()
    new_movie = MovieModel(**data.dict())
    db.add(new_movie)
    db.commit()
    db.refresh(new_movie)
    return new_movie


def get_movies():
    db = Session()
    movies = db.query(MovieModel).all()
    return movies


def get_movie(id: uuid.UUID):
    db = Session()
    movie = db.query(MovieModel).filter(MovieModel.id == id).first()
    return movie


def update_movie(id: uuid.UUID, data: MovieUpdate):
    db = Session()
    movie = db.query(MovieModel).filter(MovieModel.id == id).first()
    movie.title = data.title
    movie.overview = data.overview
    movie.year = data.year
    movie.rating = data.rating
    movie.category = data.category
    db.commit()
    db.refresh(movie)
    return movie


def delete_movie(id: uuid.UUID):
    db = Session()
    db.query(MovieModel).filter(MovieModel.id == id).first()
    db.query(MovieModel).filter(MovieModel.id == id).delete()
    db.commit()
    return
