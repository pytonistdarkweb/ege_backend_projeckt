from app.api.administration.schema import User
from app.db.repositories.user_repositories import UserRepo
from fastapi import Depends
from utils.utils import hash_password


class UserService():

    def __init__(
        self,
        user_repo: UserRepo = Depends()
    ):
        self.user_repo = user_repo

    async def create_user(self, User:User):
        """сервисный метод для создания пользователя"""
        user_dict = User.model_dump()
        user_dict["password"] = hash_password(user_dict["password"])
        return await self.user_repo.create_user(user_dict)
