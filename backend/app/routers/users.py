from fastapi import APIRouter

router = APIRouter()


@router.get("/users/{user_id}")
def get_user(user_id: int, role: str = "user"):
    return {
        "user_id": user_id,
        "role": role
    }