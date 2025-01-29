from fastapi.testclient import TestClient

#### SOLVE PATH PROBLEM ####
import sys
import os
path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),"src")
sys.path.append(path)
from main import app
############################


client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to FinanciaCore!"}