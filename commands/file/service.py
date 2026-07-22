from pathlib import Path

from config.settings import Settings


class FileService:

    @classmethod
    def ensure_temp_dir(cls):
        Settings.TEMP_DIR.mkdir(parents=True, exist_ok=True)

    @classmethod
    def validate_encrypt_attachment(cls, attachment):
        suffix = Path(attachment.filename).suffix.lower()

        if suffix not in Settings.ENCRYPT_EXTENSIONS:
            raise ValueError("Unsupported file type.")

        if attachment.size > Settings.MAX_FILE_SIZE:
            raise ValueError("File is too large.")

    @classmethod
    def validate_decrypt_attachment(cls, attachment):
        suffix = Path(attachment.filename).suffix.lower()

        if suffix not in Settings.DECRYPT_EXTENSIONS:
            raise ValueError("Only .cipher files can be decrypted.")

        if attachment.size > Settings.MAX_FILE_SIZE:
            raise ValueError("File is too large.")

    @classmethod
    async def save_encrypt_attachment(cls, attachment):
        cls.validate_encrypt_attachment(attachment)
        cls.ensure_temp_dir()

        file_path = Settings.TEMP_DIR / attachment.filename

        await attachment.save(file_path)

        return file_path

    @classmethod
    async def save_decrypt_attachment(cls, attachment):
        cls.validate_decrypt_attachment(attachment)
        cls.ensure_temp_dir()

        file_path = Settings.TEMP_DIR / attachment.filename

        await attachment.save(file_path)

        return file_path