from typing import Annotated

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from ..database.session import getSession
from ..models.company import Company
from ..schemas.auth import AccountSignUpSchema

router = APIRouter(prefix='/api/company', tags=['company'])


@router.post('/v1/sign-up', status_code=status.HTTP_201_CREATED)
def signUpCompany(
    account_data: AccountSignUpSchema,
    session: Annotated[Session, Depends(getSession)],
):
    Company.create_company(account_data, session)

    return {'message': 'Conta empresa criada com sucesse!'}
