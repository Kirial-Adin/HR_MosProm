import jwt

from fastapi import Depends

from sqlalchemy.ext.asyncio import AsyncSession

from typing import Annotated

from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError

from db.database_helper import db_helper

ph = PasswordHasher()
SECRET_KEY = settings.jwt_secret

db_session_annotated = Annotated[AsyncSession, Depends(db_helper.session_getter)]


def create_access_token(user_id: int, user_session_id: int) -> str:
    to_encode = {
        "sub": str(user_id),  # jwt lib bug: sub must be str, if not:
                              # on token validation lib raises jwt.InvalidTokenError
        "session_id": user_session_id,
    }
    return jwt.encode(to_encode, SECRET_KEY, algorithm="HS256")


def verify_token(token: str) -> dict | None:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        payload["sub"] = int(payload["sub"])  # convert back to int due bug described in create_access_token
        return payload
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None


def get_password_hash(password: str) -> str:
    return ph.hash(password)


def verify_password(hashed_password: str, password: str) -> bool:
    try:
        ph.verify(hashed_password, password)
        return True
    except VerifyMismatchError:
        return False
