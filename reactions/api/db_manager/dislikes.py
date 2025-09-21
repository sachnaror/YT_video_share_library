from YT_video_share_library.reactions.api.models import (
    CommentIn,
    CommentOut,
    DislikeIn,
    DislikeOut,
    LikeIn,
    LikeOut,
)
from YT_video_share_library.reactions.api.db import comments, dislikes, database
import os
import requests
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
from YT_video_share_library.reactions.api.user import get_current_user
from YT_video_share_library.reactions.api.videos import get_video, increase_count
from YT_video_share_library.reactions.api.db_manager.likes import add_like, delete_like, get_all_likes_by_video


async def get_dislike_by_video_and_user(video_id, username):
    query = dislikes.select().where(
        dislikes.c.video_id == video_id, dislikes.c.username == username
    )
    return await database.fetch_one(query=query)


async def get_all_dislikes_by_video(video_id):
    query = dislikes.select().where(dislikes.c.video_id == video_id)
    return await database.fetch_all(query=query)


async def add_dislike(video_id, username):
    video = await get_video(video_id)
    if not video:
        raise HTTPException("Video not found")
    query = dislikes.insert().values({"video_id": video_id, "username": username})
    id = await database.execute(query=query)
    query = dislikes.select().where(dislikes.c.id == id)
    dislike = await database.fetch_one(query=query)

    # remove like
    await delete_like(video_id, username)
    return dislike


async def delete_dislike(video_id, username):
    video = await get_video(video_id)
    if not video:
        raise HTTPException("Video not found")
    query = dislikes.delete().where(
        dislikes.c.video_id == video_id, dislikes.c.username == username
    )
    return await database.execute(query=query)


async def add_remove_dislike(video_id, user):
    video = await get_video(video_id)
    if not video:
        raise HTTPException("Video not found")
    username = user.get("username")
    dislike = await get_dislike_by_video_and_user(video_id, username)

    # toggle dislike
    if not dislike:
        dislike = await add_dislike(video_id, username)
    else:
        dislike = await delete_dislike(video_id, username)

    # count total like and dislike
    # change counts in video
    all_likes = await get_all_likes_by_video(video_id)
    all_dislikes = await get_all_dislikes_by_video(video_id)
    total_likes = len(all_likes)
    total_dislikes = len(all_dislikes)
    await increase_count(video_id, "like", total_likes)
    await increase_count(video_id, "dislike", total_dislikes)
    return dislike
