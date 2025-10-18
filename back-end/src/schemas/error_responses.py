from pydantic import BaseModel
from typing import Literal


class BaseErrorResponse(BaseModel):

    """Base for all error responses."""

    detail: str


class TokenInvalid(BaseErrorResponse):

    """Error response for invalid token."""

    detail: Literal["Invalid token", "Invalid session"]


class LogInDataInvalid(BaseErrorResponse):

    """Error response for invalid login data."""

    detail: str = "Invalid username, email or password"


class RegisterEmailConflict(BaseErrorResponse):

    """Error Response for email conflict on account registration."""

    detail: str = "Email already registered"


unauthorized = {401: {"model": TokenInvalid}}