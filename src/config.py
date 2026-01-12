from dataclasses import dataclass
from dotenv import load_dotenv
import os

load_dotenv()


@dataclass(frozen=True)
class AppConfig:
    app_name: str = os.getenv("APP_NAME", "app")
    log_level: str = os.getenv("LOG_LEVEL", "INFO")


config = AppConfig()
