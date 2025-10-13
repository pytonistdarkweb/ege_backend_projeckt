import typing

import pytest
from alembic.config import Config

from app.settings import settings
from app.tests.utils import create_test_database, drop_test_database, get_test_migrations_db_url


@pytest.fixture
async def alembic_config(anyio_backend: typing.Any):
    database_url = settings.db_url
    migration_database_url = get_test_migrations_db_url()
    await create_test_database(database_url, syffix="_test_migration")
    config = Config(file_="alembic.ini")
    config.set_main_option("script_location", "app/db/migrations")
    string_db_url = str(migration_database_url)
    config.set_section_option("alembic", "sqlalchemy.url", string_db_url)
    yield config
    await drop_test_database(database_url, syffix="_test_migration")
