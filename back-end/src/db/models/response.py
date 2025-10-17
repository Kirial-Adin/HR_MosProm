from typing import Optional, List

import sqlalchemy as sa
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base
from .enums import ResponseStatus

class Response(Base):
    """Отклик кандидата на вакансию."""

    __tablename__ = "response"

    vacancy_fk: Mapped[int] = mapped_column(
        ForeignKey("vacancy.id", ondelete="CASCADE"), nullable=False, index=True
    )
    resume_url: Mapped[Optional[str]] = mapped_column(sa.Text, nullable=True)
    first_name: Mapped[Optional[str]] = mapped_column(sa.VARCHAR, nullable=True)
    second_name: Mapped[Optional[str]] = mapped_column(sa.VARCHAR, nullable=True)
    surname: Mapped[Optional[str]] = mapped_column(sa.VARCHAR, nullable=True)

    # one-to-one: один набор contacts -> один response
    contacts_fk: Mapped[Optional[int]] = mapped_column(
        ForeignKey("contacts.id", ondelete="SET NULL"),
        nullable=True,
        unique=True,   # обеспечивает 1↔1
        index=True,
    )
    status: Mapped[ResponseStatus] = mapped_column(
        sa.Enum(ResponseStatus, name="response_status_enum", native_enum=False),
        default=ResponseStatus.PENDING,
        nullable=False,
    )

    # relations
    vacancy: Mapped["Vacancy"] = relationship(back_populates="responses")
    contacts: Mapped[Optional["Contacts"]] = relationship(
        back_populates="response", uselist=False
    )