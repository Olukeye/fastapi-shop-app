from sqlalchemy import Column, Integer, String, Boolean, BigInteger, ForeignKey
from ..utils.date_stuff import create_customised_datetime
from sqlalchemy.sql.expression import text
from ..db.database import get_db, Base
from sqlalchemy.orm import relationship
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
    owner_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    owner = relationship("User")