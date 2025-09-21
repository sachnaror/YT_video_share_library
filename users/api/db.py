

import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from databases import Database

from YT_video_share_library.users.api.models import Base

# Async driver for FastAPI runtime
DATABASE_URI = os.getenv(
    "DATABASE_URI",
    "postgresql+asyncpg://yt_user:yt_pass@localhost:5432/yt_video_db"
)

# Sync driver for Alembic migrations and ORM
SYNC_DATABASE_URI = DATABASE_URI.replace("+asyncpg", "")

# SQLAlchemy sync engine
engine = create_engine(SYNC_DATABASE_URI, echo=True)

# Session factory for ORM
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Async Database instance (used in FastAPI startup/shutdown)
database = Database(DATABASE_URI)

# Do NOT call Base.metadata.create_all(bind=engine) here.
# Alembic manages schema migrations.

# Expose metadata for Alembic to detect user models automatically
metadata = Base.metadata
