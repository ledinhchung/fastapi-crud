from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

connection_string = 'postgresql://user:{0}@postgresserver/db'
db_password = os.getenv('POSTGRES_PASSWORD')

SQLALCHEMY_DATABASE_URL = connection_string.format(db_password)

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread': False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
