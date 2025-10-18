import uuid

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from typing import Annotated
from pydantic import validate_email
from pydantic_core import PydanticCustomError

from redis.asyncio import Redis
from dishka.integrations.fastapi import FromDishka, inject

from src.db import Database
from src.db import models
from src.configuration import Configuration
from src.schemas import user
from src.schemas import error_responses

from .utils import create_access_token, get_password_hash, verify_password, verify_token


router = APIRouter(prefix="/user", tags=["user"])

@inject
async def get_account_from_token(
    redis: FromDishka[Redis],
    database: FromDishka[Database],
    config: FromDishka[Configuration],
    authorization: Annotated[HTTPAuthorizationCredentials, Depends(HTTPBearer())],
) -> models.Account | None:
    payload = verify_token(token=authorization.credentials, secret_key=config.secret_jwt)
    if not payload:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized")
    user_session = await redis.get(payload["session_id"])
    if not user_session:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized")

    return await database.account.get_by_id(obj_id=payload["sub"])

account_annotated = Annotated[models.Account, Depends(get_account_from_token)]


@router.post(
    "/registration",
    status_code=status.HTTP_201_CREATED,
    description="Create new account.",
    responses={
        status.HTTP_409_CONFLICT: {"model": error_responses.RegisterEmailConflict},
    },
)
@inject
async def sign_up(
    redis: FromDishka[Redis],
    database: FromDishka[Database],
    config: FromDishka[Configuration],
    account_in: user.SingUp,
) -> user.TokenAnswer:
    if await database.account.get_by_email(email=account_in.email):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT)

    hashed_password = get_password_hash(account_in.password)

    await database.account.new(email=account_in.email, password=hashed_password, role=account_in.role)
    user_account = await database.account.get_by_email(email=account_in.email)
    session_id = str(uuid.uuid4())
    access_token = create_access_token(user_id=user_account.id, user_session_id=session_id, secret_key=config.secret_jwt)
    await redis.set(session_id, access_token)
    return user.TokenAnswer(token=access_token)


@router.post(
    "/login",
    description="Authenticate user by email or username.",
    responses={
        status.HTTP_400_BAD_REQUEST: {
            "model": error_responses.LogInDataInvalid,
        },
    },
)
@inject
async def login(
    redis: FromDishka[Redis],
    database: FromDishka[Database],
    config: FromDishka[Configuration],
    login_payload: user.LogIn,
) -> user.TokenAnswer:
    user_account = await database.account.get_by_email(login_payload.email)

    if not user_account:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)

    if not verify_password(hashed_password=user_account.password, password=login_payload.password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)

    session_id = str(uuid.uuid4())
    access_token = create_access_token(user_id=user_account.id, user_session_id=session_id, secret_key=config.secret_jwt)
    await redis.set(session_id, access_token)
    return user.TokenAnswer(token=access_token)


@router.delete(
    "/logout",
    status_code=status.HTTP_204_NO_CONTENT,
    description="Kill current session and make token invalid. Don't affect others sessions and tokens.",
    responses=error_responses.unauthorized,
)
@inject
async def logout(
    redis: FromDishka[Redis],
    config: FromDishka[Configuration],
    authorization: Annotated[HTTPAuthorizationCredentials, Depends(HTTPBearer())]
) -> None:
    payload = verify_token(token=authorization.credentials, secret_key=config.secret_jwt)
    if not payload:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized")
    user_session = await redis.get(payload["session_id"])
    if not user_session:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized")

    await redis.delete(payload["session_id"])


@router.get(
    "/info",
    description="Get user information.",
    responses=error_responses.unauthorized,
)
async def user_info(user_account: account_annotated) -> user.UserInfoAnswer:
    return user.UserInfoAnswer(
        email=user_account.email,
    )

