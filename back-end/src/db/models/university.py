from typing import Optional, List

import sqlalchemy as sa
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

class University(Base):
    """Университет (партнёр)."""

    __tablename__ = "university"

    name: Mapped[str] = mapped_column(sa.VARCHAR, nullable=False)

    admin_fk: Mapped[Optional[int]] = mapped_column(
        ForeignKey("account.id", ondelete="SET NULL"), nullable=True, index=True
    )

    # one-to-one: один набор contacts -> один university
    contacts_fk: Mapped[Optional[int]] = mapped_column(
        ForeignKey("contacts.id", ondelete="SET NULL"),
        nullable=True,
        unique=True,   # обеспечивает 1↔1
        index=True,
    )

    # relations
    admin: Mapped[Optional["Account"]] = relationship(back_populates="admin_universities")
    contacts: Mapped[Optional["Contacts"]] = relationship(
        back_populates="university", uselist=False
    )
    requests: Mapped[List["UniversityRequest"]] = relationship(
        back_populates="university", cascade="all, delete-orphan"
    )