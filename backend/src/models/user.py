from sqlalchemy import Column, Integer, String
from ..database.database import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    name = Column(String)
    company_position = Column(String)
    hashed_password = Column(String)

    skills = Column(String)  # This should be a JSON column in a real application (apply in future versions)