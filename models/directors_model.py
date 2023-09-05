import uuid
from database import Base
from sqlalchemy import Column, UUID, String
from sqlalchemy.orm import relationship


class Director(Base):
    __tablename__ = "directors"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4())
    full_name = Column(String, unique=True, index=True)

    # Define the relationship between the Director and Movie models (one-to-many)
    movies = relationship("Movie", back_populates="director", lazy="select")
