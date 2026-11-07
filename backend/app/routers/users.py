from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class UserResponse(BaseModel):
    user_id: int
    role: str


@router.get("/users/{user_id}", response_model=UserResponse)
def get_user(user_id: int, role: str = "user"):
    return {
        "user_id": user_id,
        "role": role
    }