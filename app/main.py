from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from db import curd, schemas, models, get_db
from db.database import engine

#models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/test")
def get_root():
    return {"msg": "Hello from FastAPI!"}

@app.post("/user")
def post_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return curd.create_user(db, user)

