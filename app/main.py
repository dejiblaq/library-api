from fastapi import FastAPI
from routes.books import book_router
from routes.borrow import borrow_router
from routes.users import user_router

app = FastAPI()

app.include_router(user_router, prefix="/users", tags=["Users"])
app.include_router(book_router, prefix="/books", tags=["Books"])
app.include_router(borrow_router, prefix="/borrow", tags=["Borrow"])