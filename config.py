import os
from dotenv import load_dotenv

# load environment variables
load_dotenv()


class Config:
    PORT = os.getenv('PORT')
    DATABASE_HOST = os.getenv('DATABASE_HOST')
    DATABASE_PORT = int(os.getenv('DATABASE_PORT'))
    DATABASE_NAME = os.getenv('DATABASE_NAME')
    DATABASE_USER = os.getenv('DATABASE_USER')
    DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
    SQLALCHEMY_DATABASE_URL = "postgresql://{user}:{password}@{host}:{port}/{database}".format(
        user=DATABASE_USER,
        password=DATABASE_PASSWORD,
        host=DATABASE_HOST,
        port=DATABASE_PORT,
        database=DATABASE_NAME
    )
