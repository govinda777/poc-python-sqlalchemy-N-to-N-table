from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

class Database:
    DATABASE_URL = "mysql+pymysql://user:userpassword@localhost:3306/mydatabase"

    def __init__(self):
        self.engine = create_engine(self.DATABASE_URL)
        self.SessionLocal = sessionmaker(bind=self.engine)
        self.Base = declarative_base()

    def get_session(self):
        db = self.SessionLocal()
        try:
            yield db
        finally:
            db.close()
