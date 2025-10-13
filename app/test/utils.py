from sqlalchemy import text
from sqlalchemy.ext.asyncio import create_async_engine
from yarl import URL

from settings import settings


def get_test_db_url() -> URL:
    return URL.build(
        scheme="postgresql+asyncpg",
        host=settings.db_host,
        port=settings.db_port,
        user=settings.db_user,
        password=settings.db_pass,
        path=f"/{settings.db_base}_test",
    )


def get_test_migrations_db_url() -> URL:
    return URL.build(
        scheme="postgresql+asyncpg",
        host=settings.db_host,
        port=settings.db_port,
        user=settings.db_user,
        password=settings.db_pass,
        path=f"/{settings.db_base}_test_migration",
    )


async def create_test_database(db_url: URL, syffix: str = "_test") -> None:
    """
    Создание тестовой БД.

    :param db_url: Настройки подключения.
    """
    db_base = db_url.path.replace("/", "") + syffix
    # чтобы создать engine, должна существовать база данных db
    engine = create_async_engine(str(db_url), execution_options={"isolation_level": "AUTOCOMMIT"})
    async with engine.connect() as conn:
        database_existance = await conn.execute(text(f"SELECT 1 FROM pg_database WHERE datname='{db_base}'"))
        database_exists = database_existance.scalar() == 1
    if database_exists:
        await drop_test_database(db_url, syffix=syffix)

    async with engine.connect() as conn:
        await conn.execute(text(f"CREATE DATABASE {db_base}"))


async def drop_test_database(db_url: URL, syffix: str = "_test") -> None:
    """
    Удаление тестовой БД.

    :param db_url: Настройки подключения.
    """
    db_base = db_url.path.replace("/", "") + syffix
    engine = create_async_engine(str(db_url), execution_options={"isolation_level": "AUTOCOMMIT"})
    async with engine.connect() as conn:
        disc_users = (
            "SELECT pg_terminate_backend(pg_stat_activity.pid) "  # noqa: S608
            "FROM pg_stat_activity "
            f"WHERE pg_stat_activity.datname = '{db_base}' "
            "AND pid <> pg_backend_pid();"
        )
        await conn.execute(text(disc_users))
        await conn.execute(text(f"DROP DATABASE {db_base}"))