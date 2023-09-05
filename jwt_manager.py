from jwt import encode, decode
from config import Config


def create_token(data: dict) -> str:
    return encode(payload=data, key=Config.JWT_SECRET_KEY, algorithm='HS256')


def verify_token(token: str) -> dict:
    return decode(jwt=token, key=Config.JWT_SECRET_KEY, algorithms=['HS256'])
