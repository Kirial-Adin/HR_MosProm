from typing import Optional, List

import sqlalchemy as sa
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

class Vacancy(Base):
    """Вакансия в компании."""

    __tablename__ = "vacancy"

    name: Mapped[str] = mapped_column(sa.VARCHAR, nullable=False)

    company_fk: Mapped[int] = mapped_column(
        ForeignKey("company.id", ondelete="CASCADE"), nullable=False, index=True
    )

    tags: Mapped[Optional[dict]] = mapped_column(sa.JSON, nullable=True)
    description: Mapped[Optional[str]] = mapped_column(sa.Text, nullable=True)
    adress: Mapped[Optional[str]] = mapped_column(sa.Text, nullable=True)  # sic
    specialty: Mapped[Optional[str]] = mapped_column(sa.VARCHAR, nullable=True)

    # relations
    company: Mapped["Company"] = relationship(back_populates="vacancies")
    responses: Mapped[List["Response"]] = relationship(
        back_populates="vacancy", cascade="all, delete-orphan"
    )