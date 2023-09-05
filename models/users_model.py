import uuid
from database import Base
from sqlalchemy import Column, String, UUID
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4())
    full_name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True, index=True)
    password = Column(String, nullable=False)

    def set_encrypted_password(self) -> None:
        self.password = pwd_context.hash(self.password)

    def check_password(self, password: str) -> bool:
        return pwd_context.verify(password, self.password)
