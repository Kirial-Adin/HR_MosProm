from typing import Optional, List

import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base
from .enums import RoleEnum

class Account(Base):
    """Учетная запись пользователя (админ вуза, владелец компании, и т.п.)."""

    __tablename__ = "account"

    email: Mapped[str] = mapped_column(sa.VARCHAR(255), unique=True, nullable=False)
    password: Mapped[Optional[str]] = mapped_column(sa.Text, nullable=True)
    role: Mapped[RoleEnum] = mapped_column(
        sa.Enum(RoleEnum, name="role_enum", native_enum=False),
        nullable=False,
    )

    # relations
    owned_companies: Mapped[List["Company"]] = relationship(
        back_populates="owner", cascade="all, delete-orphan"
    )
    admin_universities: Mapped[List["University"]] = relationship(
        back_populates="admin"
    )