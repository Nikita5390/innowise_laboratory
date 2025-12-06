from fastapi import FastAPI
import uvicorn
from contextlib import asynccontextmanager
from database import create_tables, delete_tables
from router import router as books_router

WATCHFILES_FORCE_POOLING = True


@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print("Base cleaned")
    await create_tables()
    print("Base is READY")
    yield
    print("Turning off")


app = FastAPI(lifespan=lifespan)

app.include_router(books_router)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
