from pydantic import BaseModel, EmailStr

from ..utils.enums import AccountRole


class AccountSignUpSchema(BaseModel):
    username: str
    email: EmailStr
    password: str
    role: AccountRole
