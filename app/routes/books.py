from fastapi import APIRouter, HTTPException
from schemas.book_schema import Book
from services.book_service import book_service


book_router = APIRouter()

books = []


@book_router.get("/")
def get_books():
    return books

@book_router.post("/books/", response_model=Book)
def create_book(book: Book):
    books.append(book.dict())
    return book

@book_router.get("/{book_id}", response_model=Book)
def read_book(book_id: int):
    book = book_service.get_book(book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@book_router.put("/{book_id}", response_model=Book)
def update_book(book_id: int, book: Book):
    existing_book = book_service.get_book(book_id)
    if not existing_book:
        raise HTTPException(status_code=404, detail="Book not found")
    existing_book.update(book.dict())
    return existing_book

@book_router.delete("/{book_id}")
def delete_book(book_id: int):
    global books
    books = [book for book in books if book["id"] != book_id]
    return {"message": "Book deleted"}

@book_router.patch("/{book_id}/unavailable")
def mark_book_unavailable(book_id: int):
    book = book_service.get_book(book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    book["is_available"] = False
    return {"message": "Book marked as unavailable"}