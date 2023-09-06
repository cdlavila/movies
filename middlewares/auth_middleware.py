from fastapi.security import HTTPBearer
from fastapi import Request, HTTPException, status
from utils import jwt_util
from services import users_service
from schemas.users_schema import User
from models.users_model import User as UserModel


class AuthMiddleware(HTTPBearer):
    async def __call__(self, request: Request):
        auth = await super().__call__(request)
        if not auth.credentials:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='No credentials provided')

        data: dict = jwt_util.verify_token(auth.credentials)
        user: UserModel = users_service.get_user(data['id'])
        if not user:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='User no longer exists')

        request.state.user = User.from_orm(user)
