import os
from dataclasses import dataclass
from typing import Optional

try:
    from dotenv import load_dotenv

    load_dotenv()  # load .env if present
except Exception:
    pass


def _str_to_bool(v: Optional[str], default: bool = False) -> bool:
    if v is None:
        return default
    return v.lower() in {"1", "true", "yes", "on"}


@dataclass
class Settings:
    FLASK_ENV: str = os.getenv("FLASK_ENV", "development")
    SECRET_KEY: str = os.getenv("SECRET_KEY", "dev-secret-change-me")
    CORS_ORIGINS: str = os.getenv("CORS_ORIGINS", "*")
    ENABLE_SECURITY_HEADERS: bool = _str_to_bool(
        os.getenv("ENABLE_SECURITY_HEADERS"), False
    )


def get_settings() -> Settings:
    return Settings()
