from fastapi import APIRouter, HTTPException
from typing import List
from schemas.movies_schema import Movie, MovieCreate, MovieUpdate
from services import movies_service

movies_router = APIRouter()


@movies_router.post('/movies', tags=['Movies'], status_code=201)
async def create_movie(data: MovieCreate) -> Movie:
    created_movie = movies_service.create_movie(data)
    return created_movie


@movies_router.get('/movies', tags=['Movies'], status_code=200)
async def get_movies() -> List[Movie]:
    movies = movies_service.get_movies()
    return movies


@movies_router.get('/movies/{id}', tags=['Movies'], status_code=200)
async def get_movie(id: str) -> Movie:
    movie = movies_service.get_movie(id)
    if not movie:
        raise HTTPException(status_code=404, detail='Movie not found')
    return movie


@movies_router.put('/movies/{id}', tags=['Movies'], status_code=200)
async def update_movie(id: str, data: MovieUpdate) -> Movie:
    movie = movies_service.get_movie(id)
    if not movie:
        raise HTTPException(status_code=404, detail='Movie not found')
    updated_movie = movies_service.update_movie(id, data)
    return updated_movie


@movies_router.delete('/movies/{id}', tags=['Movies'], status_code=204)
async def delete_movie(id: str):
    movie = movies_service.get_movie(id)
    if not movie:
        raise HTTPException(status_code=404, detail='Movie not found')
    movies_service.delete_movie(id)
    return
