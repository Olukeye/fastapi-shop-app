from sqlalchemy import Column, Integer, String, Boolean, BigInteger, ForeignKey, Numeric
from pydantic_schemas.order import CreateOrderModel
from utils.date_stuff import create_customised_datetime
from sqlalchemy.sql.expression import text
from sqlalchemy.orm import relationship
from db.database import Base
from sqlalchemy.orm import Session
from typing import Dict, Optional


class Order(Base):
    __tablename__ = 'orders'
    id = Column(BigInteger, primary_key=True)
    user = Column(BigInteger, ForeignKey("users_id"))
    product_id = Column(BigInteger, ForeignKey('products.id'))
    first_name = Column(String, nullable=True)
    last_name = Column(String, nullable=True)
    email = Column(String, nullable=True)
    address = Column(String, nullable=True)
    zipcode = Column(Numeric, nullable=True)
    city = Column(String, nullable=True)
    phone = Column(Integer, nullable=True)
    price = Column(Numeric, nullable=False)
    quantity = Column(Integer,  nullable=False)
    created_at = Column(String, nullable=False)
    updated_at = Column(String, nullable=False)
    

    
def create_order(db: Session, order:CreateOrderModel):
    new_order = Order(user=oder.user, prodcut_id=order.product_d, first_name=order.first_name, last_name=order.email, address=order.address,
    zipcode=order.zipcode, city=order.city, phone=order.phone, price=order.price, quantity=order.quantity,created_at=create_customised_datetime(), updated_at=None)
    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    return new_order