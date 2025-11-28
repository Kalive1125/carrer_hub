from enum import Enum


class AccountRole(str, Enum):
    COMPANY = 'company'
    STUDENT = 'student'
