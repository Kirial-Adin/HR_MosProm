from __future__ import annotations

from typing import Generic, Optional, TypeVar

from sqlalchemy import delete, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import DeclarativeMeta

T = TypeVar("T")

class BaseRepo(Generic[T]):
    """Общий базовый репозиторий: get_by_id / delete."""

    model: DeclarativeMeta

    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_by_id(self, obj_id: int) -> Optional[T]:
        return await self.session.scalar(
            select(self.model).where(self.model.id == obj_id).limit(1)  # type: ignore[attr-defined]
        )

    async def delete(self, obj_id: int) -> None:
        await self.session.execute(delete(self.model).where(self.model.id == obj_id))  # type: ignore[attr-defined]
