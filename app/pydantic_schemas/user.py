from pydantic import BaseModel,EmailStr, constr
from ..utils.date_stuff import create_customised_datetime
from pydantic.types import conint
from  datetime import datetime
from decimal import Decimal
from typing import Optional


class User(BaseModel):
    username: str
    email: EmailStr
    password: constr(min_length=6, max_length=30)
    verified: Optional[bool] = None
    status: Optional[str] =  None
    role: Optional[str] = None
    created_at: Optional[str] = None
    update_at: Optional[str] = None
    
class CreateUser(User):
     pass
 
class UserOpt(BaseModel):
    id: int
    username: str
    email: EmailStr
    verified: str
    created_at: str = create_customised_datetime()
    updated_at: str = create_customised_datetime()
     
    class Config:
        orm_mode = True

class UserUpdate(BaseModel):
    username: Optional[str]
    email: Optional[EmailStr]
    
    class Config:
        orm_mode = True