from fastapi import APIRouter
from typing import List
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from schemas.movie_schema import Movie, MovieCreate, MovieUpdate
from services import movie_service

movie_router = APIRouter()


@movie_router.post('/movies', tags=['Movies'])
async def create_movie(data: MovieCreate) -> Movie:
    try:
        result = await movie_service.create_movie(data)
        return JSONResponse(status_code=201, content=jsonable_encoder(result))
    except Exception as e:
        return JSONResponse(status_code=500, content={'error': str(e)})


@movie_router.get('/movies', tags=['Movies'])
async def get_movies() -> List[Movie]:
    try:
        result = await movie_service.get_movies()
        return JSONResponse(status_code=200, content=jsonable_encoder(result))
    except Exception as e:
        return JSONResponse(status_code=500, content={'error': str(e)})


@movie_router.get('/movies/{id}', tags=['Movies'])
async def get_movie(id: str) -> Movie:
    try:
        result = await movie_service.get_movie(id)
        return JSONResponse(status_code=200, content=jsonable_encoder(result))
    except Exception as e:
        return JSONResponse(status_code=500, content={'error': str(e)})


@movie_router.put('/movies/{id}', tags=['Movies'])
async def update_movie(id: str, data: MovieUpdate) -> dict:
    try:
        await movie_service.update_movie(id, data)
        return JSONResponse(status_code=200, content=jsonable_encoder({'message': 'Movie updated successfully'}))
    except Exception as e:
        return JSONResponse(status_code=500, content={'error': str(e)})


@movie_router.delete('/movies/{id}', tags=['Movies'])
async def delete_movie(id: str) -> dict:
    try:
        await movie_service.delete_movie(id)
        return JSONResponse(status_code=200, content=jsonable_encoder({'message': 'Movie deleted successfully'}))
    except Exception as e:
        return JSONResponse(status_code=500, content={'error': str(e)})
