from sqlalchemy.orm import Session
import hashlib

from . import models, schemas

def create_user(db: Session, user: schemas.UserCreate):
    password_with_secret = '{0}secret'.format(user.password)
    md5hash = hashlib.md5(password_with_secret.endcode())
    password_hashed = md5hash.hexdigest()

    db_user = models.User(
        email = user.email,
        password = password_hashed
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user
