from __future__ import annotations

from typing import Optional, Sequence

from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession

from ..models import UniversityRequest
from .base_repo import BaseRepo


class UniversityRequestRepo(BaseRepo[UniversityRequest]):
    model = UniversityRequest

    def __init__(self, session: AsyncSession):
        super().__init__(session)

    async def new(
        self,
        university_fk: int,
        *,
        speciality: Optional[str] = None,
        group_size: Optional[int] = None,
        period: Optional[int] = None,
    ) -> None:
        await self.session.merge(
            UniversityRequest(
                university_fk=university_fk,
                speciality=speciality,
                group_size=group_size,
                period=period,
            )
        )
        await self.session.commit()

    async def list_by_university(self, university_id: int) -> Sequence[UniversityRequest]:
        result = await self.session.execute(
            select(UniversityRequest).where(UniversityRequest.university_fk == university_id)
        )
        return result.scalars().all()

    async def update_fields(
        self,
        request_id: int,
        *,
        speciality: Optional[str] = None,
        group_size: Optional[int] = None,
        period: Optional[int] = None,
    ) -> None:
        values = {}
        if speciality is not None:
            values["speciality"] = speciality
        if group_size is not None:
            values["group_size"] = group_size
        if period is not None:
            values["period"] = period
        if values:
            await self.session.execute(
                update(UniversityRequest).where(UniversityRequest.id == request_id).values(**values)
            )
