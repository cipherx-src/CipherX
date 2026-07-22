from pathlib import Path


class Settings:
    """Global project settings."""

    # Directories
    CONFIG_DIR = Path("config")
    KEYS_DIR = Path("keys")
    TEMP_DIR = Path("temp")
    OUTPUT_DIR = Path("output")

    # File Limits
    MAX_FILE_SIZE = 25 * 1024 * 1024  # 25 MB

    # Extensions
    ENCRYPT_EXTENSIONS = {
        ".txt",
        ".json",
        ".zip",
        ".py",
        ".exe",
        ".dll",
    }

    DECRYPT_EXTENSIONS = {
        ".cipher",
    }