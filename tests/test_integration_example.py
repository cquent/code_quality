# tests/test_integration_example.py
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from app import app  # or app instance, depending on your project structure


def test_health_endpoint():
    client = app.test_client()
    response = client.get("/api/hello")

    assert response.status_code == 200
    assert response.get_json() == {"message": "Hello, world!"}
