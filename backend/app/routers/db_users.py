from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, ConfigDict
from sqlalchemy.orm import Session

from backend.app.database import get_db
from backend.app import models

router = APIRouter(prefix="/db/users", tags=["Database Users"])


# Request schema
class UserCreate(BaseModel):
    name: str
    email: str


# Response schema
class UserResponse(BaseModel):
    id: int
    name: str
    email: str

    model_config = ConfigDict(from_attributes=True)


# Create a user
@router.post("/", response_model=UserResponse, status_code=201)
def create_user(user: UserCreate, db: Session = Depends(get_db)):

    existing_user = db.query(models.User).filter(
        models.User.email == user.email
    ).first()

    if existing_user:
        raise HTTPException(
            status_code=409,
            detail="Email already registered"
        )

    new_user = models.User(
        name=user.name,
        email=user.email
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


# Retrieve all users
@router.get("/", response_model=list[UserResponse])
def get_users(db: Session = Depends(get_db)):
    return db.query(models.User).all()
