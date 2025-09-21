from sqlalchemy.orm import Session
from YT_video_share_library.videos.api.db import SessionLocal
from YT_video_share_library.videos.api.models import Video, VideoIn, VideoUpdate


def create_video(video_in: VideoIn):
    db: Session = SessionLocal()
    try:
        video = Video(
            title=video_in.title,
            description=video_in.description,
            url=video_in.url,
        )
        db.add(video)
        db.commit()
        db.refresh(video)
        return video
    finally:
        db.close()


def get_video(video_id: int):
    db: Session = SessionLocal()
    try:
        return db.query(Video).filter(Video.id == video_id).first()
    finally:
        db.close()


def update_video(video_id: int, video_update: VideoUpdate):
    db: Session = SessionLocal()
    try:
        video = db.query(Video).filter(Video.id == video_id).first()
        if video:
            if video_update.title is not None:
                video.title = video_update.title
            if video_update.description is not None:
                video.description = video_update.description
            if video_update.url is not None:
                video.url = video_update.url
            db.commit()
            db.refresh(video)
        return video
    finally:
        db.close()


def delete_video(video_id: int):
    db: Session = SessionLocal()
    try:
        video = db.query(Video).filter(Video.id == video_id).first()
        if video:
            db.delete(video)
            db.commit()
        return video
    finally:
        db.close()
