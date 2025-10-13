from app.api.administration.schema import User
from base import BaseRepositories


class UserRepo(BaseRepositories):

    model = User

    async def create_user(self, user_dict: dict):
        """метод добавления пользователя в бд"""

        user = User(
            name=user_dict["name"],
            surname=user_dict["surname"],
            email=user_dict["email"],
            password=user_dict["password"],
        )
        self.session.add(user)
        await self.session.commit()
        await self.session.refresh(user)
        return user
