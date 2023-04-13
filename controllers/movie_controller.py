from fastapi import APIRouter, HTTPException
from typing import List
from fastapi.encoders import jsonable_encoder
from schemas.movie_schema import Movie, MovieCreate, MovieUpdate
from services import movie_service

movie_router = APIRouter()


@movie_router.post('/movies', tags=['Movies'], status_code=201)
async def create_movie(data: MovieCreate) -> Movie:
    created_movie = await movie_service.create_movie(data)
    return created_movie


@movie_router.get('/movies', tags=['Movies'], status_code=200)
async def get_movies() -> List[Movie]:
    movies = await movie_service.get_movies()
    return movies


@movie_router.get('/movies/{id}', tags=['Movies'], status_code=200)
async def get_movie(id: str) -> Movie:
    movie = await movie_service.get_movie(id)
    if not movie:
        raise HTTPException(status_code=404, detail='Movie not found')
    return movie


@movie_router.put('/movies/{id}', tags=['Movies'], status_code=200)
async def update_movie(id: str, data: MovieUpdate) -> Movie:
    movie = await movie_service.get_movie(id)
    if not movie:
        raise HTTPException(status_code=404, detail='Movie not found')
    updated_movie = await movie_service.update_movie(id, data)
    return updated_movie


@movie_router.delete('/movies/{id}', tags=['Movies'], status_code=204)
async def delete_movie(id: str):
    movie = await movie_service.get_movie(id)
    if not movie:
        raise HTTPException(status_code=404, detail='Movie not found')
    await movie_service.delete_movie(id)
    return
