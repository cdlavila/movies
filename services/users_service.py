from models.users_model import User as UserModel
from database import Session


def get_user(id: str) -> UserModel:
    db = Session()
    user: UserModel = db.query(UserModel.id, UserModel.full_name, UserModel.email).filter(UserModel.id == id).first()
    db.close()
    return user


def delete_user(id: str) -> None:
    db = Session()
    db.query(UserModel).filter(UserModel.id == id).delete()
    db.commit()
    db.close()
    return

