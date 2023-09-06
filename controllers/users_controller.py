from fastapi import APIRouter, dependencies, Depends, Request, HTTPException, status
from schemas.users_schema import User
from services import users_service
from middlewares.auth_middleware import AuthMiddleware

users_router = APIRouter(prefix="/users", tags=["Users"], dependencies=[Depends(AuthMiddleware())])


@users_router.get("/me", status_code=status.HTTP_200_OK)
async def get_myself(request: Request) -> User:
    user = users_service.get_user(request.state.user.id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user
