import sys
import os
from logging.config import fileConfig

from sqlalchemy import engine_from_config, create_engine
from sqlalchemy import pool

from alembic import context

# ----------------------------------------------------------------------
# 1. SETUP PATH & IMPORT
# ----------------------------------------------------------------------
sys.path.append(os.getcwd())

from app.core.config import settings  # Import settingan project
from app.models.todo import Base      # Import Base Model
# ----------------------------------------------------------------------

# Konfigurasi Alembic
config = context.config

# Setup logging
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Target Metadata untuk autogenerate
target_metadata = Base.metadata

def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode."""
    
    # PERUBAHAN: Gunakan URL langsung dari settings, jangan dari config.get_main_option
    # Ini menghindari error pembacaan karakter '%' pada password
    url = settings.DATABASE_URL
    
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

    # PERUBAHAN: Buat engine langsung menggunakan create_engine dan URL dari settings.
    # Kita tidak menggunakan engine_from_config agar tidak perlu menyimpan URL 
    # yang mengandung '%' ke dalam object config alembic.
    
    connectable = create_engine(
        settings.DATABASE_URL,
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