from __future__ import annotations

from typing import Optional

from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession

from ..models import University
from .base_repo import BaseRepo


class UniversityRepo(BaseRepo[University]):
    model = University

    def __init__(self, session: AsyncSession):
        super().__init__(session)

    async def new(
        self,
        name: str,
        *,
        admin_fk: Optional[int] = None,
        contacts_fk: Optional[int] = None,
    ) -> None:
        await self.session.merge(
            University(name=name, admin_fk=admin_fk, contacts_fk=contacts_fk)
        )

    async def get_by_name(self, name: str) -> Optional[University]:
        return await self.session.scalar(select(University).where(University.name == name).limit(1))

    async def set_contacts(self, university_id: int, contacts_id: Optional[int]) -> None:
        await self.session.execute(
            update(University).where(University.id == university_id).values(contacts_fk=contacts_id)
        )
