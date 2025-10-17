from typing import Optional

import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base


class Contacts(Base):
    """Контактные данные. Каждый объект принадлежит РОВНО одному вузу/компании/отклику."""

    __tablename__ = "contacts"

    phone: Mapped[Optional[str]] = mapped_column(sa.VARCHAR, nullable=True)
    email: Mapped[Optional[str]] = mapped_column(sa.VARCHAR, nullable=True)
    other: Mapped[Optional[str]] = mapped_column(sa.Text, nullable=True)

    university: Mapped[Optional["University"]] = relationship(
        back_populates="contacts", uselist=False
    )
    company: Mapped[Optional["Company"]] = relationship(
        back_populates="contacts", uselist=False
    )
    response: Mapped[Optional["Response"]] = relationship(
        back_populates="contacts", uselist=False
    )