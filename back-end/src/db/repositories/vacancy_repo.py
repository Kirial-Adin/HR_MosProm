from __future__ import annotations

from typing import Optional, Sequence

from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession

from ..models import Vacancy
from .base_repo import BaseRepo


class VacancyRepo(BaseRepo[Vacancy]):
    model = Vacancy

    def __init__(self, session: AsyncSession):
        super().__init__(session)

    async def new(
        self,
        name: str,
        company_fk: int,
        *,
        tags: Optional[dict] = None,
        description: Optional[str] = None,
        adress: Optional[str] = None,  # sic
        specialty: Optional[str] = None,
    ) -> None:
        await self.session.merge(
            Vacancy(
                name=name,
                company_fk=company_fk,
                tags=tags,
                description=description,
                adress=adress,
                specialty=specialty,
            )
        )
        await self.session.commit()

    async def list_by_company(self, company_id: int) -> Sequence[Vacancy]:
        result = await self.session.execute(
            select(Vacancy).where(Vacancy.company_fk == company_id)
        )
        return result.scalars().all()

    async def update_fields(
        self,
        vacancy_id: int,
        *,
        tags: Optional[dict] = None,
        description: Optional[str] = None,
        adress: Optional[str] = None,
        specialty: Optional[str] = None,
    ) -> None:
        values = {}
        if tags is not None:
            values["tags"] = tags
        if description is not None:
            values["description"] = description
        if adress is not None:
            values["adress"] = adress
        if specialty is not None:
            values["specialty"] = specialty
        if values:
            await self.session.execute(
                update(Vacancy).where(Vacancy.id == vacancy_id).values(**values)
            )
