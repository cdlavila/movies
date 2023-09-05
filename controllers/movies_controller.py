from fastapi import APIRouter, HTTPException, dependencies, Depends, Request, status
from typing import List
from schemas.movies_schema import Movie, MovieCreate, MovieUpdate
from services import movies_service
from middlewares.auth_middleware import AuthMiddleware

movies_router = APIRouter(prefix='/movies', tags=['Movies'], dependencies=[Depends(AuthMiddleware())])


@movies_router.post('/', status_code=status.HTTP_201_CREATED)
async def create_movie(data: MovieCreate) -> Movie:
    created_movie = movies_service.create_movie(data)
    return created_movie


@movies_router.get('/', status_code=status.HTTP_200_OK)
async def get_movies() -> List[Movie]:
    movies = movies_service.get_movies()
    return movies


@movies_router.get('/{id}', status_code=status.HTTP_200_OK)
async def get_movie(id: str) -> Movie:
    movie = movies_service.get_movie(id)
    if not movie:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Movie not found')
    return movie


@movies_router.put('/{id}', status_code=status.HTTP_200_OK)
async def update_movie(id: str, data: MovieUpdate) -> Movie:
    movie = movies_service.get_movie(id)
    if not movie:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Movie not found')
    updated_movie = movies_service.update_movie(id, data)
    return updated_movie


@movies_router.delete('/{id}', status_code=204)
async def delete_movie(id: str):
    movie = movies_service.get_movie(id)
    if not movie:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Movie not found')
    movies_service.delete_movie(id)
    return
