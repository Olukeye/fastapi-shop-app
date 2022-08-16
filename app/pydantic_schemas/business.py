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
    created_at: Optional[str] = None
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


class BusOpt(Business):
    id: int
    owner_id:int
    owner: UserOpt
    class Config:
        orm_mode = True
        
    