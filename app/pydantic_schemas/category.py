from pydantic import BaseModel,EmailStr, constr
from ..utils.date_stuff import create_customised_datetime
from pydantic.types import conint
from typing import Optional
from .user import UserOpt


class Category(BaseModel):
    name: str
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    
    
    
class CreateCate(Category):
    pass
    class Config:
        orm_mode = True
        

class CatOpt(BaseModel):
    name: str
    created_at: str = create_customised_datetime()
    class Config:
        orm_mode = True
        