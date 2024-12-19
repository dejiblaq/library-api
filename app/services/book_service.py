from schemas.book_schema import Book

class BookService:
    def get_book(self, books: list[Book], book_id: int):
        for book in books:
            if book["id"] == book_id:
                return book
        return None
    

book_service = BookService()