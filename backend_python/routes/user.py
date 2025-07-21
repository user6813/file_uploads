from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_all_users():
    return [{"id": 1, "name": "Alice"}]

@router.post("/")
def create_user():
    return {"message": "User created"}

@router.get("/{user_id}")
def get_user(user_id: int):
    return {"id": user_id, "name": "Alice"}

@router.put("/{user_id}")
def update_user(user_id: int):
    return {"message": f"User {user_id} updated"}

@router.delete("/{user_id}")
def delete_user(user_id: int):
    return {"message": f"User {user_id} deleted"}
