from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.asyncio import async_sessionmaker

from app.settings import settings


class DBConnector:
    _engine = None
    _session_factory = None

    @classmethod
    def get_db_url(cls):
        """
        Получить URL базы данных из настроек.
        """
        return str(settings.db_url)

    @classmethod
    def get_engine(cls):
        """
        Получить engine для подключения к базе данных.
        Создает engine только при первом вызове (Singleton паттерн).
        """
        if cls._engine is None:
            cls._engine = create_async_engine(
                cls.get_db_url(),
                max_overflow=0,
                pool_pre_ping=True
            )
        return cls._engine

    @classmethod
    def get_session_factory(cls):
        """
        Получить фабрику для создания сессий базы данных.
        Создает фабрику только при первом вызове (Singleton паттерн).
        """
        if cls._session_factory is None:
            cls._session_factory = async_sessionmaker(
                bind=cls.get_engine(),
                class_=AsyncSession,
                expire_on_commit=False,
            )
        return cls._session_factory

    @classmethod
    async def dispose(cls):
        """
        Закрыть все соединения с базой данных.
        Вызывается при завершении приложения для освобождения ресурсов.
        """
        if cls._engine:
            await cls._engine.dispose()
