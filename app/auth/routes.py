from fastapi import status, HTTPException, APIRouter, Depends
from app.users.schemas import TokenSchema, OAuth2PasswordRequestJSON
from app.config.db import conn
from app.users.models import db_user
from app.users.controllers import (
    create_access_token,
    create_refresh_token,
    verify_password
)

auth = APIRouter()


@auth.post('/login', summary="Create access and refresh tokens for user", response_model=TokenSchema)
def login(data: OAuth2PasswordRequestJSON = Depends()):
    user = conn.execute(db_user.select().where(db_user.c.email == data.username)).first()
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect email or password"
        )

    hashed_pass = user.password
    if not verify_password(data.password, hashed_pass):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect email or password"
        )

    return {
        "access_token": create_access_token(user['email']),
        "refresh_token": create_refresh_token(user['email']),
    }
