from sqlalchemy import Column, Integer, String, Boolean, BigInteger, ForeignKey, func
from ..utils.date_stuff import create_customised_datetime
from sqlalchemy.sql.expression import text
from sqlalchemy_utils import URLType
from furl import furl
from sqlalchemy.orm import relationship
from ..models.business import Business
from ..models.category import Category
from ..db.database import get_db, Base
from ..pydantic_schemas.product import *
from typing import Optional, Dict
from sqlalchemy.orm import Session


class Product(Base):
    __tablename__ = "products"
    id = Column(BigInteger, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    state = Column(String, nullable=False)
    city = Column(String, nullable=False)
    slug = Column(String, unique=True, nullable=False)
    description = Column(String, nullable=False)
    price = Column(String, nullable=False)
    url = Column(URLType)
    category = Column(BigInteger, ForeignKey("categories.id"), nullable=False)
    created_at = Column(String, server_default=text('now()'))
    updated_at = Column(String, server_default=text('now()'))
    # category = relationship("Category")

def create_new_product(db: Session, name:str=None, city:str=None,slug:str=None, description:str=None, price:str=None, category:str=None, url:str=None,created_at:str=None ):
    
    newProd = Product(name=prod.name, state=state, city=city,slug=slug, description=description, 
                                    price=price, url=url, category=category,created_at=create_customised_datetime(),updated_at=create_customised_datetime())

    db.add(newProd)
    db.commit()
    db.refresh(newProd)

    return newProd


def get_allProducts(db: Session, skip: int = 0, limit:int =10,  search: Optional[str] = ""):
    products = db.query(Product).join(Category, Category.business_id == Category.id,
        isouter=True).group_by(Product.id).filter(Product.name.contains(search)).limit(limit).offset(skip).all()
    
    return products


def get_single_product(id: int, db: Session):
    product = db.query(Product).join(Category, Category.business_id == Category.id, 
                   isouter=True).group_by(Product.id).filter(Product.id == id).first()
    
    return product


def update_product(id: int, edit: ProdUpdate, db: Session, values: Dict={}):
    values["updated_at"] = create_customised_datetime()
    
    editProduct = db.query(Product).filter(Product.id == id)
    
    editProduct.update(values)
    db.commit()
    
    return editProduct.first()


def delete_product(id: int, db: Session, user: int):
    
    delProd = db.query(Product).filter(Product.id == id)
    
    destroy = delProd.first()
    delProd.delete()
    db.commit()

    return  destroy
