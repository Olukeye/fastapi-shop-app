from pydantic import BaseModel,EmailStr, constr
from ..utils.date_stuff import create_customised_datetime
from pydantic.types import conint
from typing import Optional
from .category import CatOpt

class Product(BaseModel):
    name: str
    state: Optional[str] = None
    city: Optional[str] = None
    description: Optional[str] = None
    image: Optional[str] = None
    category_id: int
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class ProdCreate(Product):
    pass

class CatOpt(BaseModel):
    name: str
    created_at: str = create_customised_datetime()
    class Config:
        orm_mode = True
        
class ProdOpt(BaseModel):
    name: str
    state: str
    city: str
    description:str
    image: str
    category_id: int
    created_at: str = create_customised_datetime()
    class Config:
        orm_mode = True
        
class AllProd(BaseModel):
    Product: ProdOpt
    class Config:
        orm_mode = True

class ProdUpdate(BaseModel):
    name: Optional[str] = None
    state: Optional[str] = None
    city: Optional[str] = None
    description: Optional[str] = None
    logo: Optional[str] = None
    updated_at: Optional[str] = None
    
    class Config:
        orm_mode = True