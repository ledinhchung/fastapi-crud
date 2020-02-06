from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from db import curd, schemas, models
from db.database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def get_root():
    return {"msg": "Hello from FastAPI!"}
