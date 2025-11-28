from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..database.session import getSession

router = APIRouter(prefix='/auth/v1')


@router.post('/student/sign-in')
def signInStudent(session: Annotated[Session, Depends(getSession)]):
    pass


@router.post('/company/sign-in')
def signInCompany(session: Annotated[Session, Depends(getSession)]):
    pass
