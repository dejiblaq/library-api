from pydantic import BaseModel


class Book(BaseModel):
    id: int
    title: str
    author: str
    is_available: bool = True

