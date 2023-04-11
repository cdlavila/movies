from fastapi import APIRouter
from typing import List
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from src.schemas.movie_schema import Movie
from src.controllers import movie_controller

movie_router = APIRouter()


@movie_router.post('/movies', tags=['Movies'])
async def create_movie(data: Movie) -> Movie:
    try:
        result = await movie_controller.create_movie(data)
        return JSONResponse(status_code=201, content=jsonable_encoder(result))
    except Exception as e:
        return JSONResponse(status_code=500, content={'error': str(e)})


@movie_router.get('/movies', tags=['Movies'])
async def get_movies() -> List[Movie]:
    try:
        result = await movie_controller.get_movies()
        return JSONResponse(status_code=200, content=jsonable_encoder(result))
    except Exception as e:
        return JSONResponse(status_code=500, content={'error': str(e)})


@movie_router.get('/movies/{id}', tags=['Movies'])
async def get_movie(id: str) -> Movie:
    try:
        result = await movie_controller.get_movie(id)
        return JSONResponse(status_code=200, content=jsonable_encoder(result))
    except Exception as e:
        return JSONResponse(status_code=500, content={'error': str(e)})


@movie_router.put('/movies/{id}', tags=['Movies'])
async def update_movie(id: str, data: Movie) -> dict:
    try:
        await movie_controller.update_movie(id, data)
        return JSONResponse(status_code=200, content=jsonable_encoder({'message': 'Movie updated successfully'}))
    except Exception as e:
        return JSONResponse(status_code=500, content={'error': str(e)})


@movie_router.delete('/movies/{id}', tags=['Movies'])
async def delete_movie(id: str) -> dict:
    try:
        await movie_controller.delete_movie(id)
        return JSONResponse(status_code=200, content=jsonable_encoder({'message': 'Movie deleted successfully'}))
    except Exception as e:
        return JSONResponse(status_code=500, content={'error': str(e)})
