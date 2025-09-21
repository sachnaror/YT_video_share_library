import os

from sqlalchemy import Column, Integer, MetaData, String, Table, create_engine, ARRAY

from databases import Database

DATABASE_URI = (
    "postgresql://postgres:1516@localhost/reaction_db"  # os.getenv('DATABASE_URI')
)

engine = create_engine(DATABASE_URI)
metadata = MetaData()

likes = Table(
    "likes",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("video_id", Integer),
    Column("username", String(50)),
)

dislikes = Table(
    "dislikes",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("video_id", Integer),
    Column("username", String(50)),
)

comments = Table(
    "comments",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("video_id", Integer),
    Column("username", String(50)),
    Column("text", String),
)

database = Database(DATABASE_URI)
