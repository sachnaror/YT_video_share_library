"""This module handles database connections for both asynchronous FastAPI usage and synchronous Alembic/ORM operations."""

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from databases import Database
from YT_video_share_library.videos.api.models import Base

# Configuration variable for database URI
DATABASE_URI = os.getenv(
    "DATABASE_URI",
    "postgresql+asyncpg://yt_user:yt_pass@localhost:5432/yt_video_db"
)

# Async database connection (for FastAPI startup/shutdown)
database = Database(DATABASE_URI)

# Sync engine + session (for ORM & Alembic)
SYNC_DATABASE_URI = DATABASE_URI.replace("+asyncpg", "")
engine = create_engine(SYNC_DATABASE_URI, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# ORM metadata (Alembic will use this)
metadata = Base.metadata
