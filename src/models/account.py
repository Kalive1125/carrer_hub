from datetime import datetime

from fastapi import HTTPException, status
from sqlalchemy import Enum as SQLEnum
from sqlalchemy import func
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Mapped, Session, mapped_column

from ..schemas.auth import AccountSignUpSchema
from ..utils.enums import AccountRole
from .base import Base


class Account(Base):
    __tablename__ = 'accounts'

    id: Mapped[int] = mapped_column(primary_key=True, init=False)
    username: Mapped[str] = mapped_column(unique=True, nullable=False)
    email: Mapped[str] = mapped_column(unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    role: Mapped[AccountRole] = mapped_column(
        SQLEnum(AccountRole), nullable=False
    )
    created_at: Mapped[datetime] = mapped_column(
        nullable=False, server_default=func.now(), init=False
    )

    @classmethod
    def _create_account(
        cls: type['Account'],
        account_data: AccountSignUpSchema,
        session: Session,
    ) -> int:
        new_account = cls(
            username=account_data.username,
            email=account_data.email,
            password=account_data.password,
            role=account_data.role,
        )

        try:
            session.add(new_account)
            session.flush()
        except IntegrityError:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail='Email ou username já existem!',
            ) from None

        return new_account.id
