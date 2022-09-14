from fastapi import FastAPI,File, UploadFile
from pydantic import BaseModel,EmailStr, constr
from ..utils.date_stuff import create_customised_datetime
from pydantic.types import conint
from typing import Optional, List
from .category import CatOpt, Category

class Product(BaseModel):
    name: OPtional[str] = None 
    state: OPtional[str] = None 
    city: OPtional[str] = None 
    slug: OPtional[str] = None 
    description: OPtional[str] = None 
    price: OPtional[str] = None 
    image: OPtional[str] = None
    category: int 
    created_at: str = create_customised_datetime()
    updated_at: str = create_customised_datetime()
    
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
    price:int
 
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
    image: UploadFile = File(...)
    updated_at: Optional[str] = None
    
    class Config:
        orm_mode = True