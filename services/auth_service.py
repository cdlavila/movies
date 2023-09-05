from models.users_model import User as UserModel
from schemas.auth_schema import AuthRegister
from database import Session
import jwt_manager


def register(data: AuthRegister) -> UserModel:
    db = Session()
    new_user: UserModel = UserModel(**data.dict())
    new_user.set_encrypted_password()
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def validate_user_by_email(email: str) -> UserModel:
    db = Session()
    user: UserModel = db.query(UserModel).filter(UserModel.email == email).first()
    return user


def generate_access_token(user_id: str) -> str:
    return jwt_manager.create_token(data={'id': str(user_id)})
