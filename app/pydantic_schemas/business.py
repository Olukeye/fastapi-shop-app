from pydantic import BaseModel,EmailStr, constr
from ..utils.date_stuff import create_customised_datetime
from pydantic.types import conint
from typing import Optional
from .user import UserOpt


class Business(BaseModel):
    name: str
    state: str
    city: str
    description: str
    url: str
    created_at: str = create_customised_datetime()
    updated_at: str = create_customised_datetime()
    
    
class CreateBis(Business):
    class Config:
        orm_mode = True
        

class UserOpt(BaseModel):
    id: int
    username: str
    email: EmailStr
    verified: str
    created_at: str = create_customised_datetime()
    updated_at: str = create_customised_datetime()
    class Config:
        orm_mode = True


class BusOpt(Business):
    id: int
    user_id:int
    user: UserOpt
    
    class Config:
        orm_mode = True
        
        
class Allbiz(BaseModel):
    Business: BusOpt
    class Config:
        orm_mode = True

class UpdateBizz(BaseModel):
    name: Optional[str] = None
    state: Optional[str] = None
    city: Optional[str] = None
    description: Optional[str] = None
    url: Optional[str] = None
    updated_at: Optional[str] = None
    
    class Config:
        orm_mode = True