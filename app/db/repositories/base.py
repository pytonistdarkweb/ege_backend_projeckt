import typing 
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from dependencies import get_db_session


class BaseRepositories():

    model: typing.Any

    def __init__(self, session: AsyncSession = Depends(get_db_session)):
        self.session = session
