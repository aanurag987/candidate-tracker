from sqlalchemy import Column, Integer, String, Date, Enum
from sqlalchemy.sql import func
import enum

from app.database import Base

class StatusEnum(str, enum.Enum):
    applied = "Applied"
    interviewing = "Interviewing"
    rejected = "Rejected"
    hired = "Hired"

class Candidate(Base):
    __tablename__ = "candidates"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False, index=True)
    phone = Column(String, nullable=True)
    tech_stack = Column(String, nullable=False, index=True)
    status = Column(Enum(StatusEnum), default=StatusEnum.applied, nullable=False)
    applied_date = Column(Date, server_default=func.now())
    resume_link = Column(String, nullable=True)

