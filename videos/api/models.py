from typing import Optional
from pydantic import BaseModel, ConfigDict
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

# -------------------------
# ORM Models
# -------------------------
class Video(Base):
    """
    ORM model for the videos table.
    """
    __tablename__ = "videos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    description = Column(String(255), nullable=True)
    url = Column(String(255), unique=True, nullable=False)

    def __repr__(self):
        return f"<Video(id={self.id}, title={self.title})>"


# -------------------------
# Pydantic Schemas
# -------------------------

class VideoIn(BaseModel):
    title: str
    description: Optional[str] = None
    url: str


class VideoOut(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    url: str

    model_config = ConfigDict(from_attributes=True)


class VideoUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    url: Optional[str] = None


class TokenSchema(BaseModel):
    access_token: str
    token_type: str


class DetailsVideoOut(VideoOut):
    likes: int
    dislikes: int
    comments: list[str] = []

    model_config = ConfigDict(from_attributes=True)
