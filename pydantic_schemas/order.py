from pydantic import BaseModel,EmailStr, constr
from utils.date_stuff import create_customised_datetime
from pydantic.types import conint
from typing import Optional


class Order(BaseModel):
    user:int
    product_id:int
    first_name:Optional[str] = None
    last_name:Optional[str] = None
    email :Optional[str] = None
    address :Optional[str] = None
    zipcode :Optional[int] = None
    city :Optional[str] = None
    phone :Optional[int] = None
    price :Optional[float] = None
    quantity :Optional[int] = None
    
class CreateOrderModel(Order):
    pass