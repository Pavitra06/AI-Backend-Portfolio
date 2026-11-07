from fastapi import FastAPI
from backend.app.routers import users, greetings, db_users

app = FastAPI()

app.include_router(users.router)
app.include_router(greetings.router)
app.include_router(db_users.router)


@app.get("/")
def home():
    return {"message": "AI Backend Portfolio is running!"}
