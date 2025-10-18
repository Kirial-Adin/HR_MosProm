import re
import enum
from typing import Annotated

from pydantic import (
    BaseModel,
    ConfigDict,
    EmailStr,
    Field,
    AnyUrl,
)

email_annotation = Annotated[EmailStr, Field(min_length=8, max_length=120)]
password_annotation = Annotated[str, Field(min_length=8, max_length=60, pattern=re.compile(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"))] # noqa: E501
display_name_annotation = Annotated[str, Field(min_length=1, max_length=64, description="user's display name")]
telephone_number_annotation = Annotated[str, Field(min_length=1, max_length=32, description="user's telephone number")]
avatar_url_annotation = Annotated[AnyUrl, Field(description="user's avatar url")]

class RoleEnum(enum.Enum):
    COMPANY_OWNER = "company_owner"
    UNIVERSITY_ADMIN = "university_admin"

class SingUp(BaseModel):

    """Data required for SingUp (registration)."""

    model_config = ConfigDict(regex_engine="python-re")
    email: email_annotation
    password: password_annotation
    role: RoleEnum

class TokenAnswer(BaseModel):

    """Answer for auth token."""

    token: Annotated[str, Field(min_length=0, max_length=300)]

class LogIn(BaseModel):

    """Data required for LogIn.

    Attributes:
        email: email string

    """

    email: email_annotation
    password: password_annotation

class UserInfoAnswer(BaseModel):

    """Answer for non sensitivity user info."""

    email: email_annotation

class UserInfoUpdate(BaseModel):

    """Data for update info about user."""

    email: email_annotation | None = None