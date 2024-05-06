from src.schemas.user import User as UserSchemas
from src.models.models import User as UserModel
import jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta

secret_key  = "secret_key_example"
algorithm = "HS256"

# Initialize the password context for hashing passwords
password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def create_access_token(user: UserModel):
    user_obj = UserSchemas.from_orm(user)
    to_encode = user_obj.dict()
    to_encode.update({"sub": user_obj.email})
    token = jwt.encode(to_encode, secret_key)
    return dict(access_token=token, token_type="bearer")

def verify_password(plain_password, hashed_password):
    return password_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return password_context.hash(password)