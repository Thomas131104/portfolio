from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
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
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["https://my-frontend.onrender.com"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(api)

    
    return app
