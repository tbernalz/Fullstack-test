from fastapi import FastAPI
from src.database.database import Base, engine
from src.routes.api.user import router as user_router
from src.routes.api.skill import router as skill_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(user_router, prefix="/api")
app.include_router(skill_router, prefix="/api")