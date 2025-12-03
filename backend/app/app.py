from fastapi import FastAPI, Depends
from contextlib import asynccontextmanager
import asyncpg
from .database import DATABASE_URL, init_db
from .route import api


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield



def create_app():
    app = FastAPI(lifespan=lifespan)
    app.include_router(api)

    
    return app
