from datetime import date

from pydantic import BaseModel


class CreateJobSchema(BaseModel):
    title: str
    ended_in: date | None
    description: str | None
