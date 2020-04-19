import os
import sys
from logging.config import fileConfig
from sqlalchemy import engine_from_config
from sqlalchemy import pool
from alembic import context
from alembic.config import Config
from sqlalchemy.sql.schema import MetaData
from sqlalchemy.engine.base import Engine, Connection

# locate 'scooter' package manually
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

import scooter.models.__models
from scooter.models import BaseModel

config: Config = context.config
fileConfig(config.config_file_name)
target_metadata: MetaData = BaseModel.metadata


def __run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.
    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.
    Calls to context.execute() here emit the given string to the
    script output.
    """
    context.configure(
        url=config.get_main_option("sqlalchemy.url"),
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def __run_migrations_online() -> None:
    """Run migrations in 'online' mode.
    In this scenario we need to create an Engine
    and associate a connection with the context.
    """
    connectable: Engine = engine_from_config(
        config.get_section(config.config_ini_section), prefix="sqlalchemy.", poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:  # type: Connection
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()


def run_migrations() -> None:
    """Runs generic migrations."""
    if context.is_offline_mode():
        __run_migrations_offline()
    else:
        __run_migrations_online()


run_migrations()
