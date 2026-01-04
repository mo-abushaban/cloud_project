from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field, SecretStr

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        validate_default=False,
    )

    DATABRICKS_TOKEN: SecretStr | None = Field(None, env="DATABRICKS_TOKEN")
    DATABRICKS_HOST: str | None = Field(None, env="DATABRICKS_HOST")

config = Settings()
