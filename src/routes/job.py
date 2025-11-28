from typing import Annotated

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from ..database.session import getSession
from ..models.job import Job
from ..schemas.job import CreateJobSchema

router = APIRouter(prefix='/api/job', tags=['job'])


@router.post('/v1/{id}', status_code=status.HTTP_201_CREATED)
def createJob(
    id: int,
    job_data: CreateJobSchema,
    session: Annotated[Session, Depends(getSession)],
):
    Job.create_job(id, job_data, session)

    return {'message': 'Vaga criada com sucesso!'}


@router.delete('/v1/{company_id}/{job_id}')
def deleteJob(
    company_id: int,
    job_id: int,
    session: Annotated[Session, Depends(getSession)],
):
    Job.delete_job(job_id=job_id, company_id=company_id, session=session)

    return {'message': 'Vaga deletada com sucesso'}
