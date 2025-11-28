from datetime import date

from fastapi import HTTPException, status
from sqlalchemy import ForeignKey, func
from sqlalchemy.orm import Mapped, Session, mapped_column

from .base import Base
from .company import Company


class Job(Base):
    __tablename__ = 'jobs'

    id: Mapped[int] = mapped_column(primary_key=True, init=False)
    title: Mapped[str] = mapped_column(nullable=False)
    started_in: Mapped[date] = mapped_column(
        nullable=False, server_default=func.now(), init=False
    )
    ended_in: Mapped[date] = mapped_column(nullable=True)
    description: Mapped[str] = mapped_column(nullable=True)

    company_id: Mapped[int] = mapped_column(ForeignKey('companies.id'))

    @classmethod
    def create_job(cls, company_id: int, job_data: dict, session: Session):
        try:
            getCompany = session.get(Company, company_id)

            if not getCompany:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail='Empresa não encontrada',
                )

            job_data['company_id'] = company_id

            new_job = Job(**job_data)

            session.add(new_job)
            session.commit()
        except Exception:
            session.rollback()

            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail='Erro interno do servidor',
            ) from None

    @classmethod
    def update_job(cls, job_id: int, job_data_update: dict, session: Session):
        try:
            get_job = session.get(cls, job_id)

            if not get_job:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail='Vaga não encontrada!',
                )

            for key, value in job_data_update.items():
                if value is None:
                    continue

                setattr(get_job, key, value)

            session.commit()
        except Exception:
            session.rollback()

            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail='Erro interno do servidor',
            ) from None

    @classmethod
    def delete_job(cls, job_id: int, session: Session):
        try:
            get_job = session.get(cls, job_id)

            session.delete(get_job)
            session.commit()
        except Exception:
            session.rollback()

            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail='Erro interno do servidor',
            ) from None
