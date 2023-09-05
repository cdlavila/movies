import uuid
from database import Base
from sqlalchemy import Column, Integer, String, Float, UUID, ForeignKey
from sqlalchemy.orm import relationship
from .directors_model import Director


class Movie(Base):
    __tablename__ = "movies"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4())
    title = Column(String)
    overview = Column(String)
    year = Column(Integer)
    rating = Column(Float)
    category = Column(String)

    # Define the foreign key to reference the director's id
    director_id = Column(UUID(as_uuid=True), ForeignKey("directors.id"))

    # Define the relationship between the Director and Movie models (one-to-many)
    director = relationship("Director", back_populates="movies", lazy="select")

