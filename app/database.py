from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

connection_string = 'postgresql://admin:{0}@db_server:5432/db'
db_password = os.getenv('POSTGRES_PASSWORD')

SQLALCHEMY_DATABASE_URL = connection_string.format(db_password)

print SQLALCHEMY_DATABASE_URL

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
