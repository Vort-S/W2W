from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    phone : str
    name : str

user = []

@app.post("/register")
def register_user(user: User):
    users.append(user)
    return {"message": "User registered successfully"}

@app.get("/users")
def list_users():
    return users