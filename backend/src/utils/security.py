from src.schemas.user import User as UserSchemas
from src.models.user import User as UserModel
import jwt
from passlib.context import CryptContext

secret_key  = "secret_key_example"
algorithm = "HS256"
# Initialize the password context for hashing passwords
password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def create_access_token(user: UserModel):
    user_obj = UserSchemas.from_orm(user)
    token = jwt.encode(user_obj.dict(), secret_key)
    return dict(access_token=token, token_type="bearer")