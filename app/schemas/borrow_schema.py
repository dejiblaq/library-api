from pydantic import BaseModel
from datetime import date


class BorrowRecord(BaseModel):
    id: int
    user_id: int
    book_id: int
    borrow_date: date
    return_date: date | None = None