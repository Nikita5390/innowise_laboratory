from typing import Optional
from pydantic import BaseModel


class NewBookAdd(BaseModel):
    title: str
    author: str
    year: Optional[int] = None


class BookID(BaseModel):
    ok: bool
    book_id: int


class DeleteBook(BaseModel):
    ok: bool
    deleted_book_id: int


class BookUpdate(BaseModel):
    title: str | None = None
    author: str | None = None
    year: int | None = None


class BookSearch(BaseModel):
    title: str | None = None
    author: str | None = None
    year: int | None = None
