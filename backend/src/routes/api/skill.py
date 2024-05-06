from fastapi import APIRouter, Depends, HTTPException
from src.models.models import Skill as skillModel, User as UserModel
from src.schemas.skill import Skill, SkillCreate
from src.schemas.user import User
from src.database.database import get_db
from .dependencies import get_current_user

# Initialize the API router
router = APIRouter()

# Add a new skill
@router.post("/add-skill") # , response_model=Skill
def create_skill(skill: SkillCreate, db=Depends(get_db), current_user: User = Depends(get_current_user)):
    db_skill = skillModel(**skill.dict(), user_id=current_user.id)
    db.add(db_skill)
    db.commit()
    db.refresh(db_skill)
    return db_skill

# Get all user skills
@router.get("/skills")
def get_skills(db=Depends(get_db), current_user: User = Depends(get_current_user)):
    # get the skills of the User
    db_user = db.query(UserModel).filter(UserModel.id == current_user.id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user.skills