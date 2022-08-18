#  Python
from uuid import UUID

#  Pydantic
from pydantic import (BaseModel,
                      Field,
                      EmailStr,
                      validator)
#  FastAPI
from fastapi import Body, HTTPException, status


class TokenSchema(BaseModel):
    access_token: str
    refresh_token: str


class TokenPayload(BaseModel):
    sub: str = None
    exp: int = None


class User(BaseModel):
    id: int
    user_id: str
    username: str = None
    email: str
    password: str
    first_name: str = None
    last_name: str = None
    disabled: bool = False


class UserAuth(BaseModel):
    email: EmailStr
    password1: str = Field(
        min_length=8,
        max_length=50)

    password2: str = Field(
        min_length=8,
        max_length=50)

    @validator('password2')
    def passwords_match(cls, v, values, **kwargs):
        if 'password1' in values and v != values['password1']:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='passwords do not match'
            )
        return v


class UserOut(BaseModel):
    user_id: UUID
    email: str
    id: int


class OAuth2PasswordRequestJSON:

    def __init__(self, username: str = Body(), password: str = Body()):
        self.username = username
        self.password = password


class SystemUser(UserOut):
    password: str
