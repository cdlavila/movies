from .users_schema import UserBase, User
from pydantic import BaseModel, Field
from typing import Optional
import uuid


class AuthRegister(UserBase):
    pass


class AuthLogin(BaseModel):
    email: str = Field(min_length=5, max_length=50)
    password: str = Field(min_length=5, max_length=50)

    class Config:
        schema_extra = {
            "example": {
                "email": "example.user@gmail.com",
                "password": "examplepassword"
            }
        }


class AuthResponse(BaseModel):
    id: Optional[uuid.UUID] = None
    full_name: str = Field(min_length=5, max_length=50)
    email: str = Field(min_length=5, max_length=50)
    token: str

    class Config:
        schema_extra = {
            "example": {
                "id": User.Config.schema_extra['example']['id'],
                "full_name": User.Config.schema_extra['example']['full_name'],
                "email": User.Config.schema_extra['example']['email'],
                "token": "example_token"
            }
        }
