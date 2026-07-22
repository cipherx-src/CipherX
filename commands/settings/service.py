import json
from pathlib import Path


class SettingsService:
    """Business logic for the settings command."""

    CONFIG_PATH = Path("config/bot.json")

    @classmethod
    def get_settings(cls) -> dict:
        if not cls.CONFIG_PATH.exists():
            return {}

        with cls.CONFIG_PATH.open("r", encoding="utf-8") as file:
            return json.load(file)