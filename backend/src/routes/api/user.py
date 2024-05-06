from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from src.database.database import get_db
from src.models.models import User as UserModel
from src.schemas.user import User, UserCreate
from src.utils.security import create_access_token, password_context
from .dependencies import get_current_user

# Initialize the API router
router = APIRouter()

# Endpoint for signup
@router.post("/")
def create_user(user: UserCreate, db=Depends(get_db)): #db: Session = Depends(get_db)
    existing_user = db.query(UserModel).filter(UserModel.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already in use")
    hashed_password = password_context.hash(user.password.get_secret_value())
    db_user = UserModel(
        email=user.email, 
        hashed_password=hashed_password,
        name=user.name,
        company_position=user.company_position
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    access_token = create_access_token(db_user)

    return access_token

# Get a token when the user authenticates (login). Endpoint for login
@router.post("/token")
def generate_token(form_data: OAuth2PasswordRequestForm = Depends(), db=Depends(get_db)):
    user = db.query(UserModel).filter(UserModel.email == form_data.username).first()
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    password_verified = password_context.verify(form_data.password, user.hashed_password)
    if not password_verified:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    access_token = create_access_token(user)
    return access_token

@router.get("/user", response_model=User)
def read_user_me(current_user: User = Depends(get_current_user)):
    if current_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    print(f"user found: {current_user}")
    return current_user