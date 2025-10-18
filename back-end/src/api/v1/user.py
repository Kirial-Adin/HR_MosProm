from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from typing import Annotated
from pydantic import validate_email
from pydantic_core import PydanticCustomError

from src import schemas
# schemas = ...
from src.schemas import error_responses

from .utils import create_access_token, get_password_hash, verify_password, verify_token


router = APIRouter(prefix="/user", tags=["user"])


async def get_user_session_from_token(
    db_session: ... ,
    authorization: Annotated[HTTPAuthorizationCredentials, Depends(HTTPBearer())],
) -> models.UserSession | None:
    payload = verify_token(authorization.credentials)
    if not payload:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
    user_ses = await crud.user_session.get_session(session=db_session, session_id=payload["session_id"])
    if not user_ses:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid session")

    return user_ses if user_ses.user.id == payload["sub"] else None


async def get_user_from_token(
    db_session: ... ,
    authorization: Annotated[HTTPAuthorizationCredentials, Depends(HTTPBearer())],
) -> models.User:
    return (await get_user_session_from_token(db_session, authorization)).user


user_session_annotated = Annotated[models.UserSession, Depends(get_user_session_from_token)]
user_account_annotated = Annotated[models.User, Depends(get_user_from_token)]


@router.post(
    "/registration",
    status_code=status.HTTP_201_CREATED,
    description="Create new account.",
    responses={
        status.HTTP_409_CONFLICT: {"model": error_responses.RegisterEmailConflict},
    },
)
async def sign_up(
    db_session: ... ,
    account_in: schemas.user.SingUp,
) -> schemas.user.TokenAnswer:
    if await crud.user.get_account_by_email(db_session, account_in.email):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT)

    hashed_password = get_password_hash(account_in.password)
    account_in.password = hashed_password
    user_account = await crud.user.create_account(db_session, account_in)
    user_ses = await crud.user_session.create_session(db_session, user_account)
    access_token = create_access_token(user_id=user_account.id, user_session_id=user_ses.id)
    return schemas.user.TokenAnswer(token=access_token)


@router.post(
    "/login",
    description="Authenticate user by email or username.",
    responses={
        status.HTTP_400_BAD_REQUEST: {
            "model": error_responses.LogInDataInvalid,
        },
    },
)
async def login(
    db_session: ... ,
    login_payload: schemas.user.LogIn,
) -> schemas.user.TokenAnswer:
    try:
        validate_email(login_payload.login_data)
        user_account = await crud.user.get_account_by_email(db_session, login_payload.login_data)
    except PydanticCustomError:  # this exception rises by validate_email when login_data is not valid email
        user_account = await crud.user.get_account_by_username(db_session, login_payload.login_data)

    if not user_account:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)

    if not verify_password(hashed_password=user_account.password_hash, password=login_payload.password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)

    user_ses = await crud.user_session.create_session(db_session, user_account)
    access_token = create_access_token(user_id=user_account.id, user_session_id=user_ses.id)
    return schemas.user.TokenAnswer(token=access_token)


@router.delete(
    "/logout",
    status_code=status.HTTP_204_NO_CONTENT,
    description="Kill current session and make token invalid. Don't affect others sessions and tokens.",
    responses=error_responses.unauthorized,
)
async def logout(
    db_session: ... ,
    user_session: user_session_annotated,
) -> None:
    await crud.user_session.delete_session(db_session, user_session)


@router.delete(
    "/logout_others",
    status_code=status.HTTP_204_NO_CONTENT,
    description="Kill others sessions and make others tokens invalid. Don't affect on current token.",
    responses=error_responses.unauthorized,
)
async def logout_others(
    db_session: ... ,
    user_session: user_session_annotated,
) -> None:
    await crud.user_session.delete_others_sessions(db_session, user_session)


@router.get(
    "/info",
    description="Get user information.",
    responses=error_responses.unauthorized,
)
async def user_info(user_account: user_account_annotated) -> schemas.user.UserInfoAnswer:
    return schemas.user.UserInfoAnswer(
        email=user_account.email,
        username=user_account.username,
        display_name=user_account.display_name,
        telephone_number=user_account.telephone_number,
        avatar_url=user_account.avatar_url,
    )


@router.patch(
    "/update",
    description="Update user information and return updated info",
    responses=error_responses.unauthorized,
)
async def update_user(
    db_session: ... ,
    user_account: user_account_annotated,
    update_payload: schemas.user.UserInfoUpdate,
) -> schemas.user.UserInfoAnswer:
    updated_user = await crud.user.update_user_info(db_session, user_account, update_payload)
    return schemas.user.UserInfoAnswer(
        email=user_account.email,
        username=updated_user.username,
        display_name=updated_user.display_name,
        telephone_number=updated_user.telephone_number,
    )
