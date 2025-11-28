from typing import Annotated

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from ..database.session import getSession
from ..models.student import Student
from ..schemas.auth import AccountSignUpSchema

router = APIRouter(prefix='/api/student', tags=['student'])


@router.post('/v1/sign-up', status_code=status.HTTP_201_CREATED)
def signUnStudent(
    account_data: AccountSignUpSchema,
    session: Annotated[Session, Depends(getSession)],
):
    Student.create_student(account_data, session)

    return {'message': 'Conta estudante criada com sucesse!'}
