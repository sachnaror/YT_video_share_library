from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from YT_video_share_library.reactions.api.models import TokenSchema
from fastapi import APIRouter, Depends
import requests

users = APIRouter()


@users.post(
    "/token",
    summary="Create access and refresh tokens for user",
    response_model=TokenSchema,
    include_in_schema=False,
)
async def get_token(form_data: OAuth2PasswordRequestForm = Depends()):
    print("login")
    login_url = "http://localhost:8000/users/users/login"
    payload = {"username": form_data.username, "password": form_data.password}
    r = requests.post(login_url, data=payload)
    return r.json()


reuseable_oauth = OAuth2PasswordBearer(tokenUrl="/token", scheme_name="JWT")


GET_CURRENT_USER_URL = "http://localhost:8000/users/users/remote/me/"


def get_current_user(token: str = Depends(reuseable_oauth)):
    token_type = "Bearer"
    headers = {"content-type": "application/json", "Authorization": f"{token}"}
    r = requests.get(GET_CURRENT_USER_URL, headers=headers)
    return r.json()
