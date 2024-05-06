from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
import jwt
from src.database.database import get_db
from src.utils.security import secret_key, algorithm
from src.schemas.user import User, TokenData
from src.models.models import User as UserModel

credentials_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Could not validate credentials",
    headers={"WWW-Authenticate": "Bearer"},
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def get_current_user(db=Depends(get_db), token: str = Depends(oauth2_scheme)):
    print(f"Token: {token}")
    try:
        payload = jwt.decode(token, secret_key, algorithms=[algorithm])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
        token_data = TokenData(username=email)
    except jwt.DecodeError as e:
        print(f"error: {e}")
        raise credentials_exception
    user = db.query(UserModel).filter(UserModel.email == token_data.username).first()
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )
    return user
