from pydantic import BaseModel, SecretStr

class UserBase(BaseModel):
    name: str
    email: str
    company_position: str

class UserCreate(UserBase):
    password: SecretStr # User's hashed password

class User(UserBase):
    id: int

    class Config:
        orm_mode = True

class SkillBase(BaseModel):
    name: str
    level: int

class SkillCreate(SkillBase):
    pass

class Skill(SkillBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True