from fastapi import FastAPI, status, HTTPException, Depends
from fastapi.responses import RedirectResponse
from YT_video_share_library.users.api.models import TokenSchema, TokenPayload, UserAuth, UserOut, SystemUser
from YT_video_share_library.users.api import db_manager
from YT_video_share_library.users.api.utils import get_hashed_password
from uuid import uuid4
from fastapi import Header, APIRouter
from typing import List
from YT_video_share_library.users.api.models import User
from YT_video_share_library.users.api.db_manager import get_user_by_id

from fastapi.security import OAuth2PasswordRequestForm
from fastapi.responses import RedirectResponse
from YT_video_share_library.users.api.utils import (
    get_hashed_password,
    create_access_token,
    create_refresh_token,
    verify_password,
)
from uuid import uuid4
from typing import Any, Callable, Optional

import requests
from fastapi import FastAPI, Header, Response

users = APIRouter()


@users.post("/signup", summary="Create new user", response_model=UserOut)
async def create_user(data: UserAuth):
    # querying database to check if user already exist
    user = await db_manager.get_user(data.email)
    if user is not None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this email already exist",
        )
    user = {
        "email": data.email,
        "username": data.email,
        "password": get_hashed_password(data.password),
    }
    user = await db_manager.add_user(user)  # saving user to database
    return user


@users.post(
    "/login",
    summary="Create access and refresh tokens for user",
    response_model=TokenSchema,
)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await db_manager.get_user(form_data.username)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect email or password",
        )

    hashed_pass = user.password
    if not verify_password(form_data.password, hashed_pass):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect email or password",
        )

    return {
        "access_token": create_access_token(user["email"]),
        "refresh_token": create_refresh_token(user["email"]),
    }


@users.get("/all", summary="all users", response_model=List[UserOut])
async def all_user():

    return await db_manager.get_all_users()


@users.get(
    "/me", summary="Get details of currently logged in user", response_model=UserOut
)
async def get_me(user: SystemUser = Depends(db_manager.get_current_user)):
    return user


@users.get(
    "/remote/me/",
    summary="Get details of currently logged in user in remote server",
    response_model=UserOut,
)
async def get_me_remote(authorization: Optional[str] = Header(None)):
    token = authorization
    return await db_manager.get_current_user_remote(token)
