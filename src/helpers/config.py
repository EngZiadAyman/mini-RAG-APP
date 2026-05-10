from pydantic_settings import BaseSettings

class Config(BaseSettings):
    """Configuration for the application."""


    # API configuration
    api_prefix: str = "/api/v1"
    
    APP_NAME: str
    APP_VERSION: str 
    OPENAI_API_KEY: str
    FILE_ALLOWED_Types: list
    FILE_MAX_SIZE_MB: int
    FILE_CHUNK_SIZE: int


    class Config:
        env_file = ".env"


def get_config() -> Config:
    """Get the application configuration."""

    return Config()