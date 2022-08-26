from sqlalchemy import Column, Integer, String, Boolean, BigInteger, ForeignKey
from ..pydantic_schemas.product import *
from ..utils.date_stuff import create_customised_datetime
from sqlalchemy.sql.expression import text
from ..db.database import get_db, Base
from sqlalchemy.orm import relationship
from ..models.business import Business
from sqlalchemy.orm import Session
from typing import Dict


class Product(Base):
    __tablename__ = "products"
    id = Column(BigInteger, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    state = Column(String, nullable=False)
    city = Column(String, nullable=False)
    description = Column(String, nullable=False)
    image = Column(String, nullable=False)
    category_id = Column(BigInteger, ForeignKey("categories.id"), nullable=False)
    created_at = Column(String, nullable=False, server_default=text('now()'))
    updated_at = Column(String, nullable=False, server_default=text('now()'))
    business_id = Column(BigInteger, ForeignKey("businesses.id", ondelete="CASCADE"), nullable=False)
    business = relationship("Business")
    category = relationship("Category")


def create_new_product(db: Session, prod:ProdCreate):
    
    newProd = Product(name=prod.name, state=prod.state, city=prod.city, 
                      description=prod.description, image=prod.image)
    
    db.add(newProd)
    db.commit()
    db.refresh(newProd)
    
    return newProd