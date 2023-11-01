from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import models, database

from user.user_model import UserCreate

router = APIRouter()

@app.post("/users/")
def create_user(user: UserCreate, service: UserService, db: Session = Depends(get_db)):
    return crud.create_user(db=db, user=user)