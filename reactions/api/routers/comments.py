from typing import List, Union, Dict
from fastapi import Header, APIRouter, HTTPException

from YT_video_share_library.reactions.api.models import CommentOut, CommentIn
from YT_video_share_library.reactions.api.db_manager import comments as db_comments

from fastapi import Depends
import requests

comments = APIRouter()
# verify_video_owner


@comments.get(
    "/comments-by-videos",
    response_model=List[CommentOut],
    summary="All Comments by videos",
)
async def index(video_id: int):
    return await db_comments.get_all_comments_by_video(video_id)


@comments.post("/", response_model=CommentOut, summary="add comments", status_code=201)
async def add_comment(comment: CommentIn, user=Depends(db_comments.get_current_user)):
    username = user.get("username")
    return await db_comments.add_comment(comment, username)


@comments.put(
    "/{id}", response_model=CommentOut, summary="update comments", status_code=201
)
async def update_comment(id: int, text: str):
    comment = await db_comments.get_comment(id)
    if not comment:
        raise HTTPException(status_code=404, detail="Comment not found")

    return await db_comments.update_comment(id, text)


@comments.delete("/{id}", summary="Only owner can delete")
async def delete_video(x=Depends(db_comments.delete_comment)):
    return x
