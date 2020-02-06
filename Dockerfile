FROM tiangolo/uvicorn-gunicorn:python3.7

LABEL maintainer="Chung Le<ledinhchung.it@gmail.com>"

RUN pip install --upgrade pip
RUN pip install fastapi pytest requests SQLAlchemy psycopg2==2.8.4

COPY ./app /app
