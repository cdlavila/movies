from fastapi import APIRouter, HTTPException
from schemas.auth_schema import AuthRegister, AuthLogin, AuthResponse
from models.users_model import User as UserModel
from services import auth_service

auth_router = APIRouter()


@auth_router.post('/register', tags=['Auth'], status_code=201)
async def register(data: AuthRegister) -> AuthResponse:
    user: UserModel = auth_service.validate_user_by_email(data.email)
    if user:
        raise HTTPException(status_code=400, detail='Email already registered')

    created_user: UserModel = auth_service.register(data)
    token: str = auth_service.generate_access_token(created_user.id)

    return AuthResponse(
        id=str(created_user.id),
        full_name=created_user.full_name,
        email=created_user.email,
        token=token
    )


@auth_router.post('/login', tags=['Auth'], status_code=200)
async def login(data: AuthLogin) -> AuthResponse:
    user: UserModel = auth_service.validate_user_by_email(data.email)
    if not user:
        raise HTTPException(status_code=404, detail='User not found')

    if not user.check_password(data.password):
        raise HTTPException(status_code=400, detail='Incorrect password')

    token: str = auth_service.generate_access_token(user.id)
    return AuthResponse(
        id=str(user.id),
        full_name=user.full_name,
        email=user.email,
        token=token
    )
