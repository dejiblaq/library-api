from fastapi import APIRouter, HTTPException
##from app.models import users, get_user
##from app.schemas import User
from schemas.user_schema import User
from services.user_service import user_service


user_router = APIRouter()

users = []


@user_router.get("/")
def read_users():
    return users
   

@user_router.post("/", response_model=User)
def create_user(user: User):
    users.append(user.dict())
    return user

@user_router.get("/{user_id}", response_model=User)
def read_user(user_id: int):
    user = user_service.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@user_router.put("/{user_id}", response_model=User)
def update_user(user_id: int, user: User):
    existing_user = user_service.get_user(user_id)
    if not existing_user:
        raise HTTPException(status_code=404, detail="User not found")
    existing_user.update(user.dict())
    return existing_user

@user_router.delete("/{user_id}")
def delete_user(user_id: int):
    global users
    users = [user for user in users if user["id"] != user_id]
    return {"message": "User deleted"}

@user_router.patch("/{user_id}/deactivate")
def deactivate_user(user_id: int):
    user = user_service.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user["is_active"] = False
    return {"message": "User deactivated"}