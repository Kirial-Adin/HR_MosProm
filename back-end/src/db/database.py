"""Database class with all-in-one features."""

from sqlalchemy.engine.url import URL
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine as _create_async_engine

from .repositories import (
    AccountRepo,
    ContactsRepo,
    CompanyRepo,
    VacancyRepo,
    ResponseRepo,
    UniversityRepo,
    UniversityRequestRepo,
)


def create_async_engine(url: URL | str, debug: bool = False) -> AsyncEngine:
    """Create async engine with given URL.

    :param url: URL to connect
    :param debug: Enable debug
    :return: AsyncEngine
    """
    return _create_async_engine(url=url, echo=debug, pool_pre_ping=True)


class Database:
    """Database class.

    is the highest abstraction level of database and
    can be used in any functions.
    """

    session: AsyncSession
    # repo attributes
    account: AccountRepo
    contacts: ContactsRepo
    company: CompanyRepo
    vacancy: VacancyRepo
    response: ResponseRepo
    university: UniversityRepo
    university_request: UniversityRequestRepo

    def __init__(
        self,
        session: AsyncSession,
        account: AccountRepo | None = None,
        contacts: ContactsRepo | None = None,
        company: CompanyRepo | None = None,
        vacancy: VacancyRepo | None = None,
        response: ResponseRepo | None = None,
        university: UniversityRepo | None = None,
        university_request: UniversityRequestRepo | None = None,
    ):
        """Initialize Database class.

        :param session: AsyncSession to use
        :param account: (Optional) Account repository
        :param contacts: (Optional) Contacts repository
        :param company: (Optional) Company repository
        :param vacancy: (Optional) Vacancy repository
        :param response: (Optional) Response repository
        :param university: (Optional) University repository
        :param university_request: (Optional) UniversityRequest repository
        """
        self.session = session

        self.account = account or AccountRepo(session=session)
        self.contacts = contacts or ContactsRepo(session=session)
        self.company = company or CompanyRepo(session=session)
        self.vacancy = vacancy or VacancyRepo(session=session)
        self.response = response or ResponseRepo(session=session)
        self.university = university or UniversityRepo(session=session)
        self.university_request = university_request or UniversityRequestRepo(session=session)
