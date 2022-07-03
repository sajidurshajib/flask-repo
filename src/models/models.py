from sqlalchemy import Column, String, Integer
from models import BaseModel


class Role(BaseModel):
    __tablename__ = "roles"
    name = Column(String(100), nullable=False, unique=True)