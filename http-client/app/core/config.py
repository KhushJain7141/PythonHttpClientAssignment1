import os
import json
from dotenv import load_dotenv
from app.core.exceptions import ConfigError

load_dotenv()

class Config:
    def __init__(self):
        self.base_url = os.getenv("API_BASE_URL")
        self.api_key = os.getenv("API_KEY")
        self.timeout = int(os.getenv("TIMEOUT", 5))
        self.log_level = os.getenv("LOG_LEVEL", "INFO")

        headers = os.getenv("DEFAULT_HEADERS")
        self.headers = json.loads(headers) if headers else None

        self._validate()

    def _validate(self):
        if not self.base_url:
            raise ConfigError("API_BASE_URL is missing")

        if not self.api_key:
            raise ConfigError("API_KEY is missing")

        if not self.headers:
            raise ConfigError("DEFAULT_HEADERS is missing")
