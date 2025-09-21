import httpx
from YT_video_share_library.videos.api.models import Video
from YT_video_share_library.videos.api.utils import process_video

from sqlalchemy.orm import Session
from YT_video_share_library.videos.api.db import SessionLocal


def get_video_by_id(video_id: int):
    db: Session = SessionLocal()
    try:
        return db.query(Video).filter(Video.id == video_id).first()
    finally:
        db.close()


async def get_user(id):
    r = httpx.get(f"http://localhost:8000/users/users/{id}")
    return r.json()


async def get_likes(video_id):
    r = httpx.get(f"http://127.0.0.1:8003/likes/likes-by-videos?video_id={video_id}")
    likes = r.json()
    return [item["username"] for item in likes]


async def get_dislikes(video_id):
    r = httpx.get(
        f"http://127.0.0.1:8003/dislikes/dislikes-by-video?video_id={video_id}"
    )
    dislikes = r.json()
    return [item["username"] for item in dislikes]


async def get_comments(video_id):
    r = httpx.get(
        f"http://127.0.0.1:8003/comments/comments-by-videos?video_id={video_id}"
    )
    comments = r.json()
    [[item.pop("video_id"), item.pop("id")] for item in comments]
    return comments
