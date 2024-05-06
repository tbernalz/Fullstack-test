from fastapi import HTTPException
from ..models.models import User

def get_user(db, user_id: int):
    user = db.query(User).get(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user