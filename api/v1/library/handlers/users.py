from fastapi import APIRouter


users = APIRouter(prefix="/users", tags=["Users"])


@users.get("/")  # TODO admin only
def get_all_users():
    return {"message": "OK!"}


@users.post("/register/")
def register():
    pass


@users.post("/login/")
def login():
    pass


@users.post("/logout/")
def logout():
    pass
