from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from ..database.database import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    name = Column(String)
    company_position = Column(String)
    hashed_password = Column(String)

    # Define a relationship to the Skill model
    skills = relationship('Skill', back_populates='user')

class Skill(Base):
    __tablename__ = 'skills'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    level = Column(Integer)
    user_id = Column(Integer, ForeignKey('users.id'))

    # Define a relationship to the User model
    user = relationship('User', back_populates='skills')