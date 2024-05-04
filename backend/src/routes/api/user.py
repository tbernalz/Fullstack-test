from fastapi import APIRouter, Depends, HTTPException
from passlib.context import CryptContext
from src.controllers.user_controller import get_user
from src.database.database import get_db
from src.models.user import User as UserModel
from src.schemas.user import User, UserCreate
# from sqlalchemy.orm import Session

# Initialize the API router
router = APIRouter()
# Initialize the password context for hashing passwords
password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@router.post("/", response_model=User)
def create_user(user: UserCreate, db=Depends(get_db)): #db: Session = Depends(get_db)
    hashed_password = password_context.hash(user.password.get_secret_value())
    db_user = UserModel(email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@router.get("/users/{user_id}", response_model=User)
async def read_user(user_id: int, db=Depends(get_db)): # db: Session = Depends(get_db)
    db_user = db.query(UserModel).filter(UserModel.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user