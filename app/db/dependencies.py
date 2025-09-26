import typing

from fastapi.requests import Request
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.connections import DBConnector


async def get_db_session(request: Request) -> typing.AsyncGenerator[AsyncSession, None]:
    """
    метод для управления сессиями в бд
    """
    Session = DBConnector.get_session_factory()
    session = Session()
    try:
        yield session
        await session.commit()
    except Exception as e:
        await session.rollback()
        raise e
    finally:
        await session.close()
