from pydantic import BaseModel
from typing import Optional

class RoleBase(BaseModel):
    name: str

class RoleIn(RoleBase):
    pass

class RoleUpdate(BaseModel):
    name: Optional[str] = None

class RoleOut(RoleBase):
    pass 

    class Config:
        orm_mode = True