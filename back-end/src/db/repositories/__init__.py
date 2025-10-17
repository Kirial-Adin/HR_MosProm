"""Repositories package exports."""

from .base_repo import BaseRepo
from .account_repo import AccountRepo
from .contacts_repo import ContactsRepo
from .company_repo import CompanyRepo
from .vacancy_repo import VacancyRepo
from .response_repo import ResponseRepo
from .university_repo import UniversityRepo
from .university_request_repo import UniversityRequestRepo

__all__ = [
    "BaseRepo",
    "AccountRepo",
    "ContactsRepo",
    "CompanyRepo",
    "VacancyRepo",
    "ResponseRepo",
    "UniversityRepo",
    "UniversityRequestRepo",
]
