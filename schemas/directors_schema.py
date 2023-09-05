import uuid
from pydantic import BaseModel, Field
from typing import Optional


class DirectorBase(BaseModel):
    full_name: str = Field(min_length=5, max_length=50)

    class Config:
        schema_extra = {
            "example": {
                "full_name": "John Doe"
            }
        }


class Director(DirectorBase):
    id: Optional[uuid.UUID] = None

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "id": uuid.uuid4(),
                "full_name": "John Doe"
            }
        }


class DirectorCreate(DirectorBase):
    pass


class DirectorUpdate(DirectorBase):
    pass
