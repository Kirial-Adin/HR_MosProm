from __future__ import annotations

from typing import Optional

from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession

from ..models import Company
from .base_repo import BaseRepo


class CompanyRepo(BaseRepo[Company]):
    model = Company

    def __init__(self, session: AsyncSession):
        super().__init__(session)

    async def new(
        self,
        name: str,
        *,
        owner_fk: Optional[int] = None,
        logo: Optional[str] = None,
        description: Optional[str] = None,
        contacts_fk: Optional[int] = None,
    ) -> None:
        await self.session.merge(
            Company(
                name=name,
                owner_fk=owner_fk,
                logo=logo,
                description=description,
                contacts_fk=contacts_fk,
            )
        )
        await self.session.commit()

    async def get_by_name(self, name: str) -> Optional[Company]:
        return await self.session.scalar(select(Company).where(Company.name == name).limit(1))

    async def set_contacts(self, company_id: int, contacts_id: Optional[int]) -> None:
        await self.session.execute(
            update(Company).where(Company.id == company_id).values(contacts_fk=contacts_id)
        )
