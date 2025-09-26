from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """базовый класс для наследования"""
    __abstract__ = True
