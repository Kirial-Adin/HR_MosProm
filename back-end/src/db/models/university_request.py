from typing import Optional, List

import sqlalchemy as sa
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

class UniversityRequest(Base):
    """Заявка от университета на набор студентов."""

    __tablename__ = "university_request"

    speciality: Mapped[Optional[str]] = mapped_column(sa.VARCHAR, nullable=True)
    group_size: Mapped[Optional[int]] = mapped_column(sa.Integer, nullable=True)
    period: Mapped[Optional[int]] = mapped_column(sa.Integer, nullable=True)

    university_fk: Mapped[int] = mapped_column(
        ForeignKey("university.id", ondelete="CASCADE"), nullable=False, index=True
    )

    # relations
    university: Mapped["University"] = relationship(back_populates="requests")