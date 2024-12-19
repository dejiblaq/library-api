from .conftest import client, sample_user

def test_borrow_book(client):
    # First create a user and a book
    user_response = client.post("/users/", json=sample_user)
    user_id = user_response.json()["id"]
    
    book_response = client.post("/books/", json={"title": "Test Book", "author": "John Doe"})
    book_id = book_response.json()["id"]
    
    borrow_data = {"user_id": user_id, "book_id": book_id}
    response = client.post("/borrow/", json=borrow_data)
    assert response.status_code == 200
    # Assert borrowing details (implementation dependent)

def test_get_borrowing_history(client):
    # First create a borrowing record as above
    user_response = client.post("/users/", json=sample_user)
    user_id = user_response.json()["id"]
    
    book_response = client.post("/books/", json={"title": "Test Book", "author": "John Doe"})
    book_id = book_response.json()["id"]
    
    borrow_data = {"user_id": user_id, "book_id": book_id}
    _ = client.post("/borrow/", json=borrow_data)  # Create a borrowing record
    
    response = client.get(f"/users/{user_id}/borrows")
    assert response.status_code == 200
    # Assert borrowing history details (implementation dependent)