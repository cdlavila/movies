from fastapi import APIRouter, HTTPException, status
from schemas.auth_schema import AuthRegister, AuthLogin, AuthResponse
from services import auth_service

auth_router = APIRouter(prefix='/auth', tags=['Auth'])


@auth_router.post('/register', status_code=status.HTTP_201_CREATED)
async def register(data: AuthRegister) -> AuthResponse:
    user: UserModel = auth_service.validate_user_by_email(data.email)
    if user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Email already registered')

    created_user: UserModel = auth_service.register(data)
    token: str = auth_service.generate_access_token(created_user.id)

    return AuthResponse(
        id=str(created_user.id),
        full_name=created_user.full_name,
        email=created_user.email,
        token=token
    )


@auth_router.post('/login', status_code=status.HTTP_200_OK)
async def login(data: AuthLogin) -> AuthResponse:
    user: UserModel = auth_service.validate_user_by_email(data.email)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found')

    if not user.check_password(data.password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Incorrect password')

    token: str = auth_service.generate_access_token(user.id)
    return AuthResponse(
        id=str(user.id),
        full_name=user.full_name,
        email=user.email,
        token=token
    )
