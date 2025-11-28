from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..database.session import getSession

router = APIRouter(prefix='/job/v1')


@router.post('/')
def createJob(session: Annotated[Session, Depends(getSession)]): ...
