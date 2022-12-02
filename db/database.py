from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from setttings.config import settings
# import pyodbc 
# import sqlalchemy as sa



# engine = create_engine(f'mssql+pymssql://{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}?{settings.driver}')


SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# session = SessionLocal()

Base = declarative_base()

 # Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()