from pydantic import BaseModel, HttpUrl
from typing import List, Optional, Union


class CommentIn(BaseModel):
    video_id: int
    text: str


class CommentOut(CommentIn):
    id: int
    username: str


class LikeIn(BaseModel):
    video_id: int


class LikeOut(LikeIn):
    id: int
    username: str


class DislikeIn(BaseModel):
    video_id: int


class DislikeOut(DislikeIn):
    id: int
    username: str


class TokenSchema(BaseModel):
    access_token: str
    refresh_token: str
