from starlette.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_root_method():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello from FastAPI!"}
