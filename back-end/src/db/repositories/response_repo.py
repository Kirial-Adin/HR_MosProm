from __future__ import annotations

from typing import Optional, Sequence

from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession

from ..models import Response, ResponseStatus
from .base_repo import BaseRepo


class ResponseRepo(BaseRepo[Response]):
    model = Response

    def __init__(self, session: AsyncSession):
        super().__init__(session)

    async def new(
        self,
        vacancy_fk: int,
        *,
        resume_url: Optional[str] = None,
        first_name: Optional[str] = None,
        second_name: Optional[str] = None,
        surname: Optional[str] = None,
        contacts_fk: Optional[int] = None,
        status: ResponseStatus = ResponseStatus.PENDING,
    ) -> None:
        await self.session.merge(
            Response(
                vacancy_fk=vacancy_fk,
                resume_url=resume_url,
                first_name=first_name,
                second_name=second_name,
                surname=surname,
                contacts_fk=contacts_fk,
                status=status,
            )
        )
        await self.session.commit()

    async def list_by_vacancy(self, vacancy_id: int) -> Sequence[Response]:
        result = await self.session.execute(
            select(Response).where(Response.vacancy_fk == vacancy_id)
        )
        return result.scalars().all()

    async def set_status(self, response_id: int, status: ResponseStatus) -> None:
        await self.session.execute(
            update(Response).where(Response.id == response_id).values(status=status)
        )

    async def set_contacts(self, response_id: int, contacts_id: Optional[int]) -> None:
        await self.session.execute(
            update(Response).where(Response.id == response_id).values(contacts_fk=contacts_id)
        )
