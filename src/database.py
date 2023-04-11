from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm.session import sessionmaker
from src.config import Config

SQLALCHEMY_DATABASE_URL_STRUCTURE = "postgresql://{user}:{password}@{host}:{port}/{database}"
SQLALCHEMY_DATABASE_URL = SQLALCHEMY_DATABASE_URL_STRUCTURE.format(
    user=Config.DATABASE_USER,
    password=Config.DATABASE_PASSWORD,
    host=Config.DATABASE_HOST,
    port=Config.DATABASE_PORT,
    database=Config.DATABASE_NAME
)

engine = create_engine(SQLALCHEMY_DATABASE_URL)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
