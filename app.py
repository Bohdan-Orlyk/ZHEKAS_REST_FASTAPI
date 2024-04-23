import uvicorn
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.v1.library.handlers.users import users
from api.v1.library.handlers.articles import articles

from database.db import create_tables


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_tables()
    yield
    print("GOODBYE!!!")


def set_routers(app: FastAPI, routers_list: list) -> None:
    [app.include_router(router) for router in routers_list]


def set_cors(app: FastAPI, origins_list: list) -> None:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins_list,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


def init_app():
    app = FastAPI(lifespan=lifespan)

    ROUTERS = [
        users,
        articles
    ]

    origins = [
        "http://localhost:3000",
    ]
    if ROUTERS:
        set_routers(app, routers_list=ROUTERS)
    if origins:
        set_cors(app, origins_list=origins)

    return app


if __name__ == "__main__":
    uvicorn.run(app=init_app(), port=9876, host="0.0.0.0")
