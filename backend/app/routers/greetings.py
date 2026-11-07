from fastapi import APIRouter
from pydantic import BaseModel, Field

router = APIRouter()


class GreetingRequest(BaseModel):
    name: str = Field(
        min_length=2,
        max_length=30
    )


class GreetingResponse(BaseModel):
    message: str


@router.post("/greet", response_model=GreetingResponse)
def greet_user(request: GreetingRequest):
    return {
        "message": f"Hello, {request.name}!"
    }