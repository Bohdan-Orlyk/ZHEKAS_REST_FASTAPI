import uvicorn
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.v1.library.handlers.users import users
from api.v1.library.handlers.articles import articles

from database.db import create_tables

origins = [
    "http://localhost:3000",
]

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_tables()
    yield
    print("GOODBYE!!!")

app = FastAPI(lifespan=lifespan)
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


ROUTERS = [users, articles]


if __name__ == "__main__":
    [app.include_router(router) for router in ROUTERS]
    uvicorn.run(app=app)
