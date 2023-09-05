from models.users_model import User as UserModel
from schemas.users_schema import User
from database import Session


def get_user_by_email(email: str) -> User:
    db = Session()
    user = db.query(UserModel).filter(UserModel.email == email).first()
    return user
