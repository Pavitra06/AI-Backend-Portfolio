from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class UserRequest(BaseModel):
    name: str


@app.get("/")
def home():
    return {"message": "AI Backend Portfolio is running!"}


@app.post("/greet")
def greet_user(user: UserRequest):
    return {"message": f"Hello, {user.name}!"}