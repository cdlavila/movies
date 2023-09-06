import uuid
from models.directors_model import Director as DirectorModel
from schemas.directors_schema import DirectorCreate, DirectorUpdate
from database import Session
from typing import List


def create_director(director: DirectorCreate) -> DirectorModel:
    db = Session()
    new_director = DirectorModel(**director.dict())
    db.add(new_director)
    db.commit()
    db.refresh(new_director)
    db.close()
    return new_director


def get_directors() -> List[DirectorModel]:
    db = Session()
    directors = db.query(DirectorModel).all()
    db.close()
    return directors


def delete_director(id: uuid.UUID) -> None:
    db = Session()
    db.query(DirectorModel).filter(DirectorModel.id == id).delete()
    db.commit()
    db.close()
    return
