from pydantic import BaseModel

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