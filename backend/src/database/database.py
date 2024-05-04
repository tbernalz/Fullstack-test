from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from .. config.settings import DATABASE_URL

engine = create_engine(DATABASE_URL, connect_args={'check_same_thread': False})

try:
    connection = engine.connect()
    print("Connection with the database successful!")
except Exception as e:
    print("Failed to connect to the database.")
    print(e)

Base = declarative_base()

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()