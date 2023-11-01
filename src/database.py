from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

DATABASE_URL="mysql+pymysql://user:userpassword@localhost:3306/mydatabase"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

def get():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()