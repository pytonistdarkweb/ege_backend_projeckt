from pydantic_settings import SettingsConfigDict, BaseSettings
from yarl import URL


class Settings(BaseSettings):

    #параметры для приложения
    port: int = 8080
    host: str = '127.0.0.1'
    reload: bool = True

    #параметры для подключения к дб
    db_host: str = 'db'
    db_port: int = 5435
    db_user: str = 'erik'
    db_pass: str = 'erik_progger'
    db_base: str = 'postgres_ege'
    db_echo: bool = False

    @property
    def db_url(self):
        """метод для формирования урла подключения к дб"""
        return URL.build(
            scheme='postgresql+asyncpg',
            user=self.db_user,
            password=self.db_pass,
            host=self.db_host,
            port=self.db_port,
            path=f"/{self.db_base}",
        )

    model_config = SettingsConfigDict(
        env_file=".env",
        env_prefix="APP_",
        env_file_encoding="utf-8",
        extra="ignore",
    )


settings = Settings(extra="ignore")
