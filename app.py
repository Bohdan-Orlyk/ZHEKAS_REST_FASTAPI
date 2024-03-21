import uvicorn
from contextlib import asynccontextmanager

from fastapi import FastAPI

from api.v1.library.handlers.users import users
from api.v1.library.handlers.articles import articles

from database.db import create_tables


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_tables()
    yield
    print("GOODBYE!!!")

app = FastAPI(lifespan=lifespan, docs_url="/")  # TODO change to default "/docs" on prod

ROUTERS = [users, articles]


if __name__ == "__main__":
    [app.include_router(router) for router in ROUTERS]
    uvicorn.run(app=app)
