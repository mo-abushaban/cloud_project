from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field, SecretStr

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        validate_default=False,
    )

    S3_BUCKET: str = Field()
    S3_ENDPOINT: str = Field()
    AWS_ACCESS_KEY: str = Field()
    AWS_SECRET_KEY: SecretStr = Field()
    AWS_REGION: str = Field()
    EMR_CLUSTER_ID: str = Field()

config = Settings()
