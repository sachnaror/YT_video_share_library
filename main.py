from fastapi import FastAPI

from YT_video_share_library.videos.api.videos import router as videos_router
from YT_video_share_library.users.api.users import router as users_router
from YT_video_share_library.reactions.api.routers.likes import router as likes_router
from YT_video_share_library.reactions.api.routers.dislikes import router as dislikes_router
from YT_video_share_library.reactions.api.routers.comments import router as comments_router

from YT_video_share_library.videos.api.db import database

app = FastAPI(title="YT Video Share Library")

# Routers
app.include_router(videos_router, prefix="/videos", tags=["Videos"])
app.include_router(users_router, prefix="/users", tags=["Users"])
app.include_router(likes_router, prefix="/likes", tags=["Likes"])
app.include_router(dislikes_router, prefix="/dislikes", tags=["Dislikes"])
app.include_router(comments_router, prefix="/comments", tags=["Comments"])

# Database lifecycle
@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
