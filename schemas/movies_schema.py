import uuid
from pydantic import BaseModel, Field
from typing import Optional


class MovieBase(BaseModel):
    title: Optional[str] = Field(min_length=5, max_length=15)
    overview: Optional[str] = Field(min_length=5, max_length=50)
    year: Optional[int] = Field(le=2023)
    rating: Optional[float] = Field(ge=1, le=10)
    category: Optional[str] = Field(min_length=5, max_length=25)

    class Config:
        schema_extra = {
            "example": {
                "title": "Example movie",
                "overview": "Example overview",
                "year": 2023,
                "rating": 9.8,
                "category": "Example category"
            },
        }


class Movie(MovieBase):
    id: Optional[uuid.UUID] = None

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "id": uuid.uuid4(),
                "title": "Example movie",
                "overview": "Example overview",
                "year": 2023,
                "rating": 9.8,
                "category": "Example category"
            },
        }


class MovieCreate(MovieBase):
    pass


class MovieUpdate(MovieBase):
    pass
