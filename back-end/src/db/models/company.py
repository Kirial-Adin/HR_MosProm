from typing import Optional, List

import sqlalchemy as sa
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base


class Company(Base):
    """Компания-работодатель."""

    __tablename__ = "company"

    name: Mapped[str] = mapped_column(sa.VARCHAR, nullable=False)

    owner_fk: Mapped[Optional[int]] = mapped_column(
        ForeignKey("account.id", ondelete="SET NULL"), nullable=True, index=True
    )
    logo: Mapped[Optional[str]] = mapped_column(sa.Text, nullable=True)
    description: Mapped[Optional[str]] = mapped_column(sa.Text, nullable=True)

    contacts_fk: Mapped[Optional[int]] = mapped_column(
        ForeignKey("contacts.id", ondelete="SET NULL"),
        nullable=True,
        unique=True,   # обеспечивает 1↔1
        index=True,
    )

    # relations
    owner: Mapped[Optional["Account"]] = relationship(back_populates="owned_companies")
    contacts: Mapped[Optional["Contacts"]] = relationship(
        back_populates="company", uselist=False
    )
    vacancies: Mapped[List["Vacancy"]] = relationship(
        back_populates="company", cascade="all, delete-orphan"
    )