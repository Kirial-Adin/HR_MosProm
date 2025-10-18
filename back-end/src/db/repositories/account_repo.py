from __future__ import annotations

from typing import Optional

from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession

from ..models import Account, RoleEnum
from .base_repo import BaseRepo


class AccountRepo(BaseRepo[Account]):
    model = Account

    def __init__(self, session: AsyncSession):
        super().__init__(session)

    async def new(
        self,
        email: str,
        password: str,
        role: RoleEnum
    ) -> None:
        await self.session.merge(Account(email=email, password=password, role=role))
        await self.session.commit()

    async def get_by_email(self, email: str) -> Optional[Account]:
        return await self.session.scalar(select(Account).where(Account.email == email).limit(1))

    async def update_password(self, account_id: int, password: Optional[str]) -> None:
        await self.session.execute(
            update(Account).where(Account.id == account_id).values(password=password)
        )
