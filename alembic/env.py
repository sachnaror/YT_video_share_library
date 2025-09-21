"""This file configures Alembic migrations for the YT_video_share_library project."""

from logging.config import fileConfig
import os

from sqlalchemy import engine_from_config, pool
from alembic import context

# Import your ORM Base and database configuration
from YT_video_share_library.videos.api.models import Base
from YT_video_share_library.videos.api.db import DATABASE_URI

# Alembic Config object
config = context.config

# Set database URL from imported configuration
config.set_main_option("sqlalchemy.url", DATABASE_URI)

# Logging
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Target metadata for autogenerate
# Alembic will manage migrations and schemas for these metadata objects
target_metadata = [Base.metadata]
# You can add multiple metadata here for other apps as needed, e.g.:
# target_metadata = [Base.metadata, UsersBase.metadata, ReactionsBase.metadata]


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
