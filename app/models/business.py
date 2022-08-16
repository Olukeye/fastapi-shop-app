from sqlalchemy import Column, Integer, String, Boolean, BigInteger, ForeignKey
from ..pydantic_schemas.business import CreateBis, BusOpt
from ..utils.date_stuff import create_customised_datetime
from sqlalchemy.sql.expression import text
from sqlalchemy.orm import relationship
from ..db.database import get_db, Base
from sqlalchemy.orm import Session
from ..models.user import User
from typing import Dict


class Business(Base):
    __tablename__ = "businesses"
    id = Column(BigInteger, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    state = Column(String, nullable=False)
    city = Column(String, nullable=False)
    description = Column(String, nullable=False)
    logo = Column(String, nullable=False)
    created_at = Column(String, nullable=False, server_default=text('now()'))
    updated_at = Column(String, nullable=False, server_default=text('now()'))
    owner_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    owner = relationship("User")
    
    

def create_new_business(db: Session, user:int,  reg:CreateBis):
    
    newBusiness = Business(name=reg.name, state=reg.state, city=reg.city, description=reg.description,
                           logo=reg.logo, created_at=create_customised_datetime(), updated_at=create_customised_datetime())
    
    db.add(newBusiness)
    db.commit()
    db.refresh(newBusiness)
    
    
    return newBusiness