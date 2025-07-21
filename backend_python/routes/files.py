from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_all_files():
    return [{"id": 1, "name": "Alice"}]

@router.post("/")
def create_file():
    return {"message": "File created"}

@router.get("/{file_id}")
def get_file(file_id: int):
    return {"id": file_id, "name": "Alice"}

@router.put("/{file_id}")
def update_file(file_id: int):
    return {"message": f"File {file_id} updated"}

@router.delete("/{file_id}")
def delete_file(file_id: int):
    return {"message": f"File {file_id} deleted"}
