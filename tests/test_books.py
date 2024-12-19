from .conftest import client

def test_create_book(client):
    book_data = {"title": "Test Book", "author": "John Doe"}
    response = client.post("/books/", json=book_data)
    assert response.status_code == 200
    assert response.json()["title"] == book_data["title"]

def test_get_book(client):
    # First create a book
    create_response = client.post("/books/", json={"title": "Test Book", "author": "John Doe"})
    book_id = create_response.json()["id"]
    
    get_response = client.get(f"/books/{book_id}")
    assert get_response.status_code == 200
    assert get_response.json()["title"] == "Test Book"

def test_update_book(client):
    # Create a book first
    create_response = client.post("/books/", json={"title": "Test Book", "author": "John Doe"})
    book_id = create_response.json()["id"]
    
    update_data = {"title": "Updated Title"}
    response = client.put(f"/books/{book_id}", json=update_data)
    assert response.status_code == 200
    assert response.json()["title"] == update_data["title"]

def test_delete_book(client):
    # Create a book first
    create_response = client.post("/books/", json={"title": "Test Book", "author": "John Doe"})
    book_id = create_response.json()["id"]
    
    response = client.delete(f"/books/{book_id}")
    assert response.status_code == 200
    assert client.get(f"/books/{book_id}").status_code == 404

def test_mark_book_unavailable(client):
    # Create a book first
    create_response = client.post("/books/", json={"title": "Test Book", "author": "John Doe"})
    book_id = create_response.json()["id"]
    
    response = client.patch(f"/books/{book_id}/unavailable")
    assert response.status_code == 200
    # Assert the book's availability status (implementation dependent)