import enum

class RoleEnum(enum.Enum):
    ADMIN = "admin"
    COMPANY_OWNER = "company_owner"
    UNIVERSITY_ADMIN = "university_admin"

class ResponseStatus(enum.Enum):
    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"