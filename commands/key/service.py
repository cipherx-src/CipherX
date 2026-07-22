from pathlib import Path

from cryptography.fernet import Fernet
from config.settings import Settings

class KeyService:
    """Business logic for key management."""

    @classmethod
    def get_key_path(cls, guild_id: int):
     Settings.KEYS_DIR.mkdir(parents=True, exist_ok=True)

     return Settings.KEYS_DIR / f"{guild_id}.key"

    @classmethod
    def has_key(cls, guild_id: int) -> bool:
        return cls.get_key_path(guild_id).exists()

    @classmethod
    def generate_key(cls, guild_id: int) -> str:
        key = Fernet.generate_key().decode()

        key_path = cls.get_key_path(guild_id)

        key_path.write_text(
            key,
            encoding="utf-8"
        )

        return key

    @classmethod
    def get_key(cls, guild_id: int) -> str | None:
        key_path = cls.get_key_path(guild_id)

        if not key_path.exists():
            return None

        return key_path.read_text(
            encoding="utf-8"
        ).strip()

    @classmethod
    def ensure_key(cls, guild_id: int) -> tuple[bool, str]:
        """
        Returns:
            (created, key)
        """

        key = cls.get_key(guild_id)

        if key is not None:
            return False, key

        key = cls.generate_key(guild_id)

        return True, key

    @classmethod
    def delete_key(cls, guild_id: int) -> bool:
        key_path = cls.get_key_path(guild_id)

        if not key_path.exists():
            return False

        key_path.unlink()

        return True

    @classmethod
    def rotate_key(cls, guild_id: int) -> str:
        cls.delete_key(guild_id)

        return cls.generate_key(guild_id)