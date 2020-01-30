FROM tiangolo/uvicorn-gunicorn:python3.7-alpine3.8

LABEL maintainer="Chung Le<ledinhchung.it@gmail.com>"

RUN pip install fastapi pytest requests

COPY ./app /app
