from models.users_model import User as UserModel
from schemas.auth_schema import AuthRegister, AuthLogin, AuthResponse
from schemas.users_schema import User
from database import Session
import jwt_manager


def register(data: AuthRegister) -> User:
    data.set_encrypted_password()
    db = Session()
    new_user: UserModel = UserModel(**data.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def generate_access_token(user_id: str) -> str:
    return jwt_manager.create_token(data={'id': str(user_id)})
