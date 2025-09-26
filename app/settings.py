from pydantic_settings import SettingsConfigDict, BaseSettings


class Settings(BaseSettings):

    port: int = 8080
    host: str = '127.0.0.1'
    reload: bool = True

    model_config = SettingsConfigDict(
        env_file=".env",
        env_prefix="APP_",
        env_file_encoding="utf-8",
        extra= "ignore",
    )

settings = Settings(extra="ignore")
