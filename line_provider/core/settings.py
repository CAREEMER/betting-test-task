from pydantic import AnyUrl, BaseSettings


class Settings(BaseSettings):
    bet_maker_url: AnyUrl = "http://localhost:8000"


app_settings = Settings()
