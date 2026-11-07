from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class UserRequest(BaseModel):
    name: str


@app.get("/")
def home():
    return {"message": "AI Backend Portfolio is running!"}


@app.get("/users/{user_id}")
def get_user(user_id: int, role: str = "user"):
    return {
        "user_id": user_id,
        "role": role
    }


@app.post("/greet")
def greet_user(user: UserRequest):
    return {"message": f"Hello, {user.name}!"}