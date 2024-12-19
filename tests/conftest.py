import pytest
from fastapi.testclient import TestClient
from app.main import app

@pytest.fixture
def client():
    with TestClient(app) as c:
        yield c

# Example fixture to load sample data (e.g., a user)
@pytest.fixture
def sample_user():
    return {"name": "Test User", "email": "test@example.com"}