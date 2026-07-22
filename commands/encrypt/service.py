from pathlib import Path

from config.settings import Settings
from commands.key.service import KeyService
from services.crypto.aes import AESService


class EncryptService:

    @classmethod
    def ensure_output_dir(cls):
        Settings.OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    @classmethod
    def encrypt(cls, guild_id: int, input_path: Path) -> Path:
        cls.ensure_output_dir()

        key = KeyService.get_key(guild_id)

        if key is None:
            raise ValueError("No encryption key found.")

        output_path = Settings.OUTPUT_DIR / f"{input_path.name}.cipher"

        AESService.encrypt_file(
            input_path=input_path,
            output_path=output_path,
            key=key,
        )

        return output_path