from pydantic import BaseModel,EmailStr, constr
from ..utils.date_stuff import create_customised_datetime
from pydantic.types import conint
from typing import Optional
from .user import UserOpt


class Business(BaseModel):
    name: str
    state: str
    city: str
    description: Optional[str] = None
    logo: Optional[str] = None
    created_at: Optional[str]
    update_at: Optional[str] = None
    
    
class CreateBis(Business):
    pass

class UserOpt(BaseModel):
    id: int
    username: str
    email: EmailStr
    verified: str
    created_at: str = create_customised_datetime
    updated_at: str = create_customised_datetime
    class Config:
        orm_mode = True


class BusOpt(BaseModel):
    id: int
    name: str
    state: str
    city: str
    description: str
    created_at: str = create_customised_datetime
    updated_at: str = create_customised_datetime
    
    class Config:
        orm_mode = True
        
    