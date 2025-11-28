from typing import Annotated

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from ..database.session import getSession

router = APIRouter(prefix='/api/auth/v1')


@router.post('/student/sign-in', status_code=status.HTTP_201_CREATED)
def signInStudent(
    session: Annotated[Session, Depends(getSession)],
): ...
@router.post('/company/sign-in')
def signInCompany(session: Annotated[Session, Depends(getSession)]):
    pass
