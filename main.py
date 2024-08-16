from fastapi import FastAPI, HTTPException, Query, Path
from pydantic import BaseModel
from typing import Optional, List
from uuid import UUID, uuid4

app = FastAPI()

# Sample in-memory database
users_db = {}

# Pydantic model for User
class User(BaseModel):
    name: str
    email: str
    age: Optional[int] = None

# Add a new user
@app.post("/users")
def add_user(user: User):
    user_id = str(uuid4())
    users_db[user_id] = user
    return {"user_id": user_id, "user": user}

# Retrieve users with pagination
@app.get("/users", response_model=List[User])
def get_users(page: int = 1, limit: int = 10):
    start = (page - 1) * limit
    end = start + limit
    users_list = list(users_db.values())[start:end]
    return users_list

# Search users by name or email
@app.get("/users/search", response_model=List[User])
def search_users(query: str = Query(..., min_length=1)):
    results = [user for user in users_db.values() if query.lower() in user.name.lower() or query.lower() in user.email.lower()]
    return results

# Update user details
@app.put("/users/{user_id}")
def update_user(user_id: str = Path(...), user: User = ...):
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    users_db[user_id] = user
    return {"user_id": user_id, "user": user}

# Delete a user
@app.delete("/users/{user_id}")
def delete_user(user_id: str):
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    del users_db[user_id]
    return {"detail": "User deleted"}
