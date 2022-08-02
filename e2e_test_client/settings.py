from pydantic import AnyUrl, BaseSettings


class Settings(BaseSettings):
    bet_maker_url: AnyUrl = "http://localhost:8000"
    line_provider_url: AnyUrl = "http://localhost:8001"


app_settings = Settings()
