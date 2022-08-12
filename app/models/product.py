# from sqlalchemy import Column, Integer, String, Boolean, BigInteger, ForeignKey
# from ..utils.date_stuff import create_customised_datetime
# from sqlalchemy.sql.expression import text
# from ..db.database import get_db, Base
# from sqlalchemy.orm import relationship
# from ..models.business import Business
# from typing import Dict


# class Product(Base):
#     __tablename__ = "products"
#     id = Column(BigInteger, primary_key=True, nullable=False)
#     name = Column(String, nullable=False)
#     state = Column(String, nullable=False)
#     city = Column(String, nullable=False)
#     description = Column(String, nullable=False)
#     image = Column(String, nullable=False)
#     business_id = Column(Integer, ForeignKey("businesses.id", ondelete="CASCADE"), nullable=False)
#     business_owner = relationship("Business")