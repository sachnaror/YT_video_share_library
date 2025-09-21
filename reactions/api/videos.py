from fastapi import APIRouter, Depends, HTTPException
import httpx
from YT_video_share_library.reactions.api.models import ReactionVideo


GET_VIDEO_URL = "http://localhost:8002/videos/videos/"
INCREASE_COUNT = "http://localhost:8002/videos/videos/change_count"


async def get_video(id: int):
    r = httpx.get(f"{GET_VIDEO_URL}{id}")
    if r.status_code != 200:
        raise HTTPException(400)
    return r.json()


async def increase_count(id: int, object_type, total_count):
    r = httpx.get(
        f"{INCREASE_COUNT}/{id}?object_type={object_type}&total_count={total_count}"
    )
