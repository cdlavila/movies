from fastapi import APIRouter, HTTPException, dependencies, Depends, status
from typing import List
from schemas.directors_schema import Director, DirectorCreate, DirectorUpdate
from services import directors_service
from middlewares.auth_middleware import AuthMiddleware

directors_router = APIRouter(prefix="/directors", tags=["Directors"], dependencies=[Depends(AuthMiddleware())])


@directors_router.post("/", status_code=status.HTTP_201_CREATED)
async def create_director(data: DirectorCreate) -> Director:
    created_director = directors_service.create_director(data)
    return created_director


@directors_router.get("/", status_code=status.HTTP_200_OK)
async def get_directors() -> List[Director]:
    directors = directors_service.get_directors()
    return directors
