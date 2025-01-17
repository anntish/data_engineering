from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .prompt_model import Base
import os

DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():

    try:
        Base.metadata.create_all(bind=engine)
        return engine
    except Exception as e:
        raise

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()