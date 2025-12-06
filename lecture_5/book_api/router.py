from fastapi import APIRouter, Depends, HTTPException
from typing import Annotated
from typing import Optional
from schemas import NewBookAdd, BookID, BookUpdate, BookSearch
from repository import BookRepository

router = APIRouter(
    prefix="/books",
)


@router.post("")
async def add_books(
        book: Annotated[NewBookAdd, Depends()],
) -> BookID:
    book_id = await BookRepository.add_one(book)
    return {"ok": True, "book_id": book_id}


@router.get("")
async def get_books():
    books = await BookRepository.find_all()
    return {"books": books}


@router.delete("/{book_id}")
async def delete_book(book_id: int):
    deleted = await BookRepository.delete_one(book_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Book not found")
    return {"ok": True, "deleted_id": book_id}


@router.put("/{book_id}")
async def update_book(book_id: int, data: BookUpdate):
    updated = await BookRepository.update_one(book_id, data)
    if not updated:
        raise HTTPException(status_code=404, detail="Книга не найдена")
    return {"status": "success", "book_id": book_id}


@router.get("/search")
async def search_books(
        title: Optional[str] = None,
        author: Optional[str] = None,
        year: Optional[int] = None
):
    filters = BookSearch(title=title, author=author, year=year)
    books = await BookRepository.find_by_filters(filters)
    return books
