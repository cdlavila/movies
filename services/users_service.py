from models.users_model import User as UserModel
from database import Session


def get_by_id(id: str) -> UserModel:
    db = Session()
    user: UserModel = db.query(UserModel.id, UserModel.full_name, UserModel.email).filter(UserModel.id == id).first()
    db.close()
    return user
