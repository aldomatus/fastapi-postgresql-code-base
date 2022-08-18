from fastapi import status, HTTPException, APIRouter, Depends
from app.users.schemas import UserOut, UserAuth, User
from app.users.deps import get_current_user
from app.config.db import conn
from app.users.controllers import get_hashed_password
from app.users.models import db_user

users = APIRouter()


@users.post('/signup', summary="Create new user", response_model=UserOut)
async def create_user(data: UserAuth):
    # querying database to check if user already exist
    user = conn.execute(db_user.select().where(db_user.c.email == data.email)).first()
    if user is not None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this email already exists"
        )

    new_user = {
        'email': data.email,
        'password': get_hashed_password(data.password1)
    }
    # saving user to database
    result = conn.execute(db_user.insert().values(new_user))
    return conn.execute(db_user.select().where(db_user.c.id == result.lastrowid)).first()


@users.get('/protected', summary='Get details of currently logged in user', response_model=UserOut)
async def get_protected_function(user: User = Depends(get_current_user)):
    return user
