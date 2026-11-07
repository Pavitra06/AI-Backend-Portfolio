from fastapi import FastAPI
from backend.app.routers import users, greetings

app = FastAPI()

app.include_router(users.router)
app.include_router(greetings.router)


@app.get("/")
def home():
    return {"message": "AI Backend Portfolio is running!"}