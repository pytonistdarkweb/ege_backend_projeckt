from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy.types import String
from db.base import Base


class User(Base):
    __tablename__ = 'User'

    id: Mapped[int] = mapped_column(primary_key=True, comment='уникальный идентификатор')
    name: Mapped[str] = mapped_column(String(length=25), nullable=False, comment='имя пользователя')
    surname: Mapped[str] = mapped_column(String(length=25), nullable=False, comment='фамилия пользователя')
    password: Mapped[str] = mapped_column(nullable=False, comment='пароль пользователя')
    email: Mapped[str] = mapped_column(nullable=False, comment='почтовый адрес пользователя')
