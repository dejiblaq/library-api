from fastapi import APIRouter, HTTPException
from schemas.borrow_schema import BorrowRecord
from services.borrow_service import borrow_service
from services.book_service import book_service
from services.user_service import user_service


from datetime import date

borrow_router = APIRouter()

borrow_records = []


@borrow_router.post("/", response_model=BorrowRecord)
def borrow_book(user_id: int, book_id: int):
    user = user_service.get_user(user_id)
    if not user or not user["is_active"]:
        raise HTTPException(status_code=400, detail="User is inactive or doesn't exist")
    
    book = book_service.get_book(book_id)
    if not book or not book["is_available"]:
        raise HTTPException(status_code=400, detail="Book is unavailable or doesn't exist")
    
    existing_record = next((r for r in borrow_records if r["user_id"] == user_id and r["book_id"] == book_id), None)
    if existing_record:
        raise HTTPException(status_code=400, detail="User has already borrowed this book")
    
    new_record = {
        "id": len(borrow_records) + 1,
        "user_id": user_id,
        "book_id": book_id,
        "borrow_date": date.today()
    }
    borrow_records.append(new_record)
    book["is_available"] = False
    return new_record

@borrow_router.patch("/{record_id}")
def return_book(record_id: int):
    record = borrow_service.get_borrow_record(record_id)
    if not record:
        raise HTTPException(status_code=404, detail="Borrow record not found")
    
    book = book_service.get_book(record["book_id"])
    if book:
        book["is_available"] = True
    
    record["return_date"] = date.today()
    return {"message": "Book returned successfully"}

@borrow_router.get("/borrowing-records/user/{user_id}")
def get_user_borrowing_records(user_id: int):
    user = user_service.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    records = [r for r in borrow_records if r["user_id"] == user_id]
    return records

@borrow_router.get("/borrowing-records/")
def get_all_borrowing_records():
    return borrow_records