import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fastapi.testclient import TestClient
from app import app
# import pytest

client = TestClient(app)

def test_app_root():
    res = client.get("/")
    assert res.status_code == 200
    assert res.json() == {"Hello": "World"}
    
def test_app_error():
    res = client.get("/error")
    assert res.status_code == 401
    assert res.json() == {'detail': 'Item not found'}
    

