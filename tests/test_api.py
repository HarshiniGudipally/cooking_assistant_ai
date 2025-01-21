import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from fastapi.testclient import TestClient
from backend.app import app

client = TestClient(app)

def test_query_endpoint():
    response = client.post("/chat", json={"session_id": "test_session", "content": "How do I make pasta?"})
    assert response.status_code == 200
    assert "response" in response.json()

def test_history_endpoint():
    response = client.get("/history/test_session")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
