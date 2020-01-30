from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def get_root():
    return {"msg": "Hello from FastAPI!"}
