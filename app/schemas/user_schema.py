from pydantic import BaseModel
from datetime import date

class User(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool = True


