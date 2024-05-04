from fastapi import FastAPI
from src.database.database import Base, engine
from src.routes.api.user import router as UserRouter

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(UserRouter, prefix="/api")