from pydantic import BaseModel, EmailStr
from datetime import date
from app.models import StatusEnum

class CandidateBase(BaseModel):
    name: str
    email: EmailStr
    phone: str | None = None
    tech_stack: str
    resume_link: str | None = None

class CandidateCreate(CandidateBase):
    pass    

class CandidateUpdateStatus(BaseModel):
    status: StatusEnum

class CandidateResponse(CandidateBase):
    id: int
    status: StatusEnum
    applied_date: date

    class Config:
        from_attributes = True
