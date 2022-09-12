from pydantic import BaseModel,EmailStr, constr
from ..utils.date_stuff import create_customised_datetime
from pydantic.types import conint
from typing import Optional, List
from .category import CatOpt, Category

class Product(BaseModel):
    name: Optional[str] 
    state: Optional[str] 
    city: Optional[str] 
    slug: Optional[str] 
    description: Optional[str] 
    price: Optional[str] 
    url: Optional[str] 
    category: Optional[int] 
    created_at: Optional[str] = create_customised_datetime()
    updated_at: Optional[str] = create_customised_datetime()
    
class ProdCreate(Product):
    pass
        

class CatOpt(BaseModel):
    id:int
    name: str
    created_at: str = create_customised_datetime()
    class Config:
        orm_mode = True
        
class ProdOpt(BaseModel):
    name: str
    state: str
    city: str
    slug: str
    description:str
    price:str
    url: str
    category: int
    # category: CatOpt
    created_at: str = create_customised_datetime()
    updated_at: str=  create_customised_datetime()
    class Config:
        orm_mode = True
        
class AllProd(BaseModel):
    Product: ProdOpt
    categories: CatOpt 
    class Config:
        orm_mode = True

class ProdUpdate(BaseModel):
    name: str
    description: Optional[str] = None
    price:Optional[float] = None
    url: Optional[str] = None
    updated_at: Optional[str] = None
    
    class Config:
        orm_mode = True