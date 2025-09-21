"""
This module provides CRUD operations and authentication helpers for user management,
including proper password hashing for secure storage, using SQLAlchemy and FastAPI.
"""
from typing import Union, Any
from datetime import datetime

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from jose.exceptions import JWTError  # ✅ correct import for error handling
from pydantic import ValidationError
from sqlalchemy.orm import Session

from YT_video_share_library.users.api.models import (
    TokenSchema,
    TokenPayload,
    UserAuth,
    UserOut,
    SystemUser,
    User,              # ORM model
    UserCreate,        # Pydantic schema for user creation
    UserUpdate         # Pydantic schema for user update
)
from YT_video_share_library.users.api.db import SessionLocal
from YT_video_share_library.users.api.utils import ALGORITHM, JWT_SECRET_KEY

# Password hashing
from passlib.hash import bcrypt


# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ---------------------------
# CRUD FUNCTIONS (now with password hashing)
# ---------------------------
def add_user(db: Session, user_in: UserCreate) -> User:
    hashed_password = bcrypt.hash(user_in.password)
    user = User(
        email=user_in.email,
        username=user_in.username,
        password=hashed_password,   # 🔑 Password is hashed before saving
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def get_all_users(db: Session):
    return db.query(User).all()


def get_user_by_email(db: Session, email: str) -> Union[User, None]:
    return db.query(User).filter(User.email == email).first()


def get_user_by_id(db: Session, id: int) -> Union[User, None]:
    return db.query(User).filter(User.id == id).first()


def delete_user(db: Session, id: int) -> bool:
    user = db.query(User).filter(User.id == id).first()
    if not user:
        return False
    db.delete(user)
    db.commit()
    return True


def update_user(db: Session, id: int, payload: UserUpdate) -> Union[User, None]:
    user = db.query(User).filter(User.id == id).first()
    if not user:
        return None
    for field, value in payload.dict(exclude_unset=True).items():
        setattr(user, field, value)
    db.commit()
    db.refresh(user)
    return user


# ---------------------------
# AUTH HELPERS
# ---------------------------

reuseable_oauth = OAuth2PasswordBearer(tokenUrl="/users/users/login", scheme_name="JWT")


def get_user_from_token(token: str, db: Session) -> SystemUser:
    try:
        payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[ALGORITHM])
        token_data = TokenPayload(**payload)

        if datetime.fromtimestamp(token_data.exp) < datetime.now():
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token expired",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except (JWTError, ValidationError):   # ✅ fixed
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

    user = get_user_by_email(db, token_data.sub)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Could not find user",
        )

    return SystemUser.from_orm(user)


def get_current_user(token: str = Depends(reuseable_oauth), db: Session = Depends(get_db)) -> SystemUser:
    return get_user_from_token(token, db)


def get_current_user_remote(token: str, db: Session) -> SystemUser:
    return get_user_from_token(token, db)
