from sqlalchemy.orm import Session
from . import models, domain_entities

class UserService:
    def __init__(self, db: Session):
        self.db = db

    def get_user(self, user_id: int) -> domain_entities.UserEntity:
        db_user = self.db.query(models.UserModel).filter(models.UserModel.id == user_id).first()
        if db_user:
            return domain_entities.UserEntity(id=db_user.id, name=db_user.name, groups=[group.id for group in db_user.groups])
        return None

    def get_users(self, skip: int = 0, limit: int = 10) -> list[domain_entities.UserEntity]:
        db_users = self.db.query(models.UserModel).offset(skip).limit(limit).all()
        return [domain_entities.UserEntity(id=user.id, name=user.name, groups=[group.id for group in user.groups]) for user in db_users]

    def create_user(self, user: domain_entities.UserEntity) -> domain_entities.UserEntity:
        db_user = models.UserModel(name=user.name)  # Assuming groups are handled separately
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        user.id = db_user.id
        return user

    def update_user(self, user: domain_entities.UserEntity) -> domain_entities.UserEntity:
        db_user = self.db.query(models.UserModel).filter(models.UserModel.id == user.id).first()
        if db_user:
            db_user.name = user.name  # Update other fields as needed
            self.db.commit()
            self.db.refresh(db_user)
            return user
        return None

    def delete_user(self, user_id: int) -> bool:
        db_user = self.db.query(models.UserModel).filter(models.UserModel.id == user_id).first()
        if db_user:
            self.db.delete(db_user)
            self.db.commit()
            return True
        return False
