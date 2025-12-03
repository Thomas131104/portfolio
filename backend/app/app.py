from fastapi import FastAPI
from contextlib import asynccontextmanager
import asyncpg
from .database import DATABASE_URL, init_db
from .route import api

from fastapi import FastAPI
from contextlib import asynccontextmanager
from .database import init_db
from .route import api

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield



def create_app():
    app = FastAPI(lifespan=lifespan)
    app.include_router(api)

    @app.get("/users")
    async def get_users():
        async with app.state.pool.acquire() as conn:
            rows = await conn.fetch("SELECT id, name, email, content, method FROM users")
            return [dict(row) for row in rows]
    
    return app
