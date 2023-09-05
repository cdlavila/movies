import uuid
from pydantic import BaseModel, Field
from typing import Optional


class UserBase(BaseModel):
    full_name: str = Field(min_length=5, max_length=50)
    email: str = Field(min_length=5, max_length=50)
    password: str = Field(min_length=5, max_length=50)

    class Config:
        schema_extra = {
            "example": {
                "full_name": "Example user",
                "email": "example.user@gmail.com",
                "password": "examplepassword"
            },
        }


class User(UserBase):
    id: Optional[uuid.UUID] = None

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "id": uuid.uuid4(),
                "full_name": "Example user",
                "email": "example.user@gmail.com",
                "password": "$2b$11$4kNQve4IRy8y/BsvfWQHpeLWEcct9jdvJy6QSCwS/m.Hu.2n5JMBi",
            },
        }
