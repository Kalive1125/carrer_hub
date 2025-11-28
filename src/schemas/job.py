from datetime import date

from pydantic import BaseModel


class PostJobSchema(BaseModel):
    title: str
    ended_in: date
    description: str
