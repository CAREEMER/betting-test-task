from pydantic import AnyUrl, BaseSettings, RedisDsn


class Settings(BaseSettings):
    line_provider_url: AnyUrl = "http://localhost:8001"
    redis_dsn: RedisDsn = "redis://localhost:6379"


app_settings = Settings()
