import jwt
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError

ph = PasswordHasher()

def create_access_token(user_id: int, user_session_id: str, secret_key: str) -> str:
    to_encode = {
        "sub": str(user_id),  # jwt lib bug: sub must be str, if not:
                              # on token validation lib raises jwt.InvalidTokenError
        "session_id": user_session_id,
    }
    return jwt.encode(to_encode, secret_key, algorithm="HS256")

def verify_token(token: str, secret_key: str) -> dict | None:
    try:
        payload = jwt.decode(token, secret_key, algorithms=["HS256"])
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