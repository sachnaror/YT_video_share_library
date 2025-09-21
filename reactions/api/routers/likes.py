from typing import List, Union, Dict
from fastapi import Header, APIRouter, HTTPException

from YT_video_share_library.reactions.api.models import LikeIn, LikeOut
from YT_video_share_library.reactions.api.db_manager import likes as db_likes

from fastapi import Depends
import requests

likes = APIRouter()
# verify_video_owner


@likes.get(
    "/likes-by-videos", response_model=List[LikeOut], summary="All Likes by videos"
)
async def index(video_id: int):
    return await db_likes.get_all_likes_by_video(video_id)


@likes.post(
    "/add-remove-likes",
    response_model=Union[LikeOut, None],
    summary="Toggle like button and remove dislike",
    status_code=201,
)
async def add_remove_like(id: int, user=Depends(db_likes.get_current_user)):
    return await db_likes.add_remove_like(id, user)
