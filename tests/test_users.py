from fastapi import HTTPException
from app.schemas import UserCreate
from .conftest import client, sample_user

def test_create_user(client):
    response = client.post("/users/", json=sample_user)
    assert response.status_code == 200
    assert response.json()["email"] == sample_user["email"]

def test_get_user(client):
    # First create a user
    create_response = client.post("/users/", json=sample_user)
    user_id = create_response.json()["id"]
    
    get_response = client.get(f"/users/{user_id}")
    assert get_response.status_code == 200
    assert get_response.json()["email"] == sample_user["email"]

def test_update_user(client):
    # Create a user first
    create_response = client.post("/users/", json=sample_user)
    user_id = create_response.json()["id"]
    
    update_data = {"name": "Updated Name"}
    response = client.put(f"/users/{user_id}", json=update_data)
    assert response.status_code == 200
    assert response.json()["name"] == update_data["name"]

def test_delete_user(client):
    # Create a user first
    create_response = client.post("/users/", json=sample_user)
    user_id = create_response.json()["id"]
    
    response = client.delete