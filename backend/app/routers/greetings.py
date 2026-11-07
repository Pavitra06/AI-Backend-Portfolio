from fastapi import APIRouter
from pydantic import BaseModel, Field

router = APIRouter()


class GreetingRequest(BaseModel):
    name: str = Field(
        min_length=2,
        max_length=30
    )


@router.post("/greet")
def greet_user(request: GreetingRequest):
    return {
        "message": f"Hello, {request.name}!"
    }