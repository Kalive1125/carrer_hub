from datetime import datetime

from fastapi import HTTPException, status
from sqlalchemy import ForeignKey, String, func
from sqlalchemy.orm import Mapped, mapped_column, Session

from .base import Base


class Inscription(Base):
    __tablename__ = 'inscriptions'

    jobopening_id: Mapped[int] = mapped_column(
        ForeignKey('job_openings.id'), primary_key=True
    )
    student_id: Mapped[int] = mapped_column(
        ForeignKey('students.id'), primary_key=True
    )
    why: Mapped[str] = mapped_column(String(500), nullable=True)
    created_at: Mapped[datetime] = mapped_column(
        nullable=False, server_default=func.now(), init=False
    )

    @classmethod
    def create_inscription(cls, jobopening_id: int, student_id: int,
                           data_inscription: dict, session: Session
    ):
        inscription = session.get(Inscription, (jobopening_id, student_id))

        if inscription:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail='Inscrição ja existe'
            )
        
        new_inscription = cls(
            student_id = student_id,
            jobopening_id = jobopening_id,
            **data_inscription
        )

        session.add(new_inscription)
        session.commit()

    @classmethod
    def update_inscription(cls): ...

    @classmethod
    def delete_inscription(cls): ...
