from __future__ import annotations

from typing import Optional

from sqlalchemy import update
from sqlalchemy.ext.asyncio import AsyncSession

from ..models import Contacts
from .base_repo import BaseRepo


class ContactsRepo(BaseRepo[Contacts]):
    model = Contacts

    def __init__(self, session: AsyncSession):
        super().__init__(session)

    async def new(
        self,
        phone: Optional[str] = None,
        email: Optional[str] = None,
        other: Optional[str] = None,
    ) -> None:
        await self.session.merge(Contacts(phone=phone, email=email, other=other))
        await self.session.commit()

    async def update_fields(
        self,
        contacts_id: int,
        *,
        phone: Optional[str] = None,
        email: Optional[str] = None,
        other: Optional[str] = None,
    ) -> None:
        values = {}
        if phone is not None:
            values["phone"] = phone
        if email is not None:
            values["email"] = email
        if other is not None:
            values["other"] = other
        if values:
            await self.session.execute(
                update(Contacts).where(Contacts.id == contacts_id).values(**values)
            )
