from database import new_session, BooksOrm
from schemas import NewBookAdd, BookUpdate, BookSearch
from sqlalchemy import select, delete, update


class BookRepository:
    @classmethod
    async def add_one(cls, data: NewBookAdd):
        async with new_session() as session:
            book_dict = data.model_dump()
            book = BooksOrm(**book_dict)
            session.add(book)
            await session.flush()
            await session.commit()
            return book.id

    @classmethod
    async def find_all(cls):
        async with new_session() as session:
            query = select(BooksOrm)
            result = await session.execute(query)
            books_models = result.scalars().all()
            return books_models

    @classmethod
    async def delete_one(cls, book_id: int) -> bool:
        async with new_session() as session:
            result = await session.execute(select(BooksOrm).where(BooksOrm.id == book_id))
            book = result.scalar_one_or_none()
            if not book:
                return False
            await session.execute(delete(BooksOrm).where(BooksOrm.id == book_id))
            await session.commit()
            return True

    @classmethod
    async def update_one(cls, book_id: int, data: BookUpdate) -> bool:
        async with new_session() as session:
            # check book
            result = await session.execute(select(BooksOrm).where(BooksOrm.id == book_id))
            book = result.scalar_one_or_none()
            if not book:
                return False

            # update only new data
            update_data = data.model_dump(exclude_unset=True)
            await session.execute(
                update(BooksOrm)
                .where(BooksOrm.id == book_id)
                .values(**update_data)
            )
            await session.commit()
            return True

    @classmethod
    async def find_by_filters(cls, filters: BookSearch):
        async with new_session() as session:
            query = select(BooksOrm)
            if filters.title:
                query = query.where(BooksOrm.title.ilike(f"%{filters.title}%"))
            if filters.author:
                query = query.where(BooksOrm.author.ilike(f"%{filters.author}%"))
            if filters.year:
                query = query.where(BooksOrm.year == filters.year)
            result = await session.execute(query)
            books = result.scalars().all()
            return books
