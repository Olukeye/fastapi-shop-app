from sqlalchemy import Column, Integer, String, Boolean, BigInteger, ForeignKey
from pydantic_schemas.business import CreateBis, BusOpt, UpdateBizz
from utils.date_stuff import create_customised_datetime
from sqlalchemy.sql.expression import text
from sqlalchemy_utils import URLType
from sqlalchemy.orm import relationship
from db.database import get_db, Base
from sqlalchemy.orm import Session
from models.user import User
from typing import Dict, Optional


class Business(Base):
    __tablename__ = "businesses"
    id = Column(BigInteger, primary_key=True, nullable=False)
    name = Column(String, unique=True, nullable=False)
    state = Column(String, nullable=False)
    city = Column(String, nullable=False)
    description = Column(String, nullable=False)
    # url = Column(URLType, nullable=True)
    created_at = Column(String, nullable=False, server_default=text('now()'))
    updated_at = Column(String, nullable=False, server_default=text('now()'))
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    user = relationship("User")
    
    

def create_new_business(db: Session, user:int,  reg:CreateBis):
    
    newBusiness = Business(name=reg.name, state=reg.state, city=reg.city, description=reg.description,
                            created_at=create_customised_datetime(), updated_at=create_customised_datetime(), user=user)
    
    db.add(newBusiness)
    db.commit()
    db.refresh(newBusiness)
    
    return newBusiness



def get_all_business(db: Session,  limit: int = 3, skip: int = 2, search: Optional[str] = ""):
    
    get_all = db.query(Business).filter(Business.name.contains(search)).limit(limit).offset(skip).all()
    
    return get_all


def get_a_business(db: Session, id: int):
    
    singleBusiness = db.query(Business).filter(Business.id == id).first()
    
    return singleBusiness 
    
    
def update_business(id: int, edit:UpdateBizz, db: Session, values: Dict={}):
    
    values["updated_at"] = json.dumps(create_customised_datetime())
    
    updated = db.query(Business).filter(Business.id == id)
    
    updated.update(values)
    db.commit()
    
    return updated.first()