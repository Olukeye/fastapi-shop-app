from pydantic import BaseModel,EmailStr, constr
from utils.date_stuff import create_customised_datetime
from pydantic.types import conint
from typing import Optional
from .user import UserOpt


class Business(BaseModel):
    name: Optional[str] = None
    state: Optional[str] = None
    city: Optional[str] = None
    description: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    
    
class CreateBis(Business):
    pass

class UserOpt(BaseModel):
    id: int
    username: str
    email: EmailStr
    # verified: str
    class Config:
        orm_mode = True


class BusOpt(Business):
    id: int
    user: UserOpt
    class Config:
        orm_mode = True
        
class UpdateBizz(BaseModel):
    name: Optional[str] = None
    state: Optional[str] = None
    city: Optional[str] = None
    description: Optional[str] = None
    
    class Config:
        orm_mode = True