from pathlib import Path

from cryptography.fernet import Fernet


class AESService:
    """Handles file encryption and decryption."""

    @staticmethod
    def encrypt_file(input_path: Path, output_path: Path, key: str):
        cipher = Fernet(key.encode())

        data = input_path.read_bytes()

        encrypted = cipher.encrypt(data)

        output_path.write_bytes(encrypted)

    @staticmethod
    def decrypt_file(input_path: Path, output_path: Path, key: str):
        cipher = Fernet(key.encode())

        data = input_path.read_bytes()

        decrypted = cipher.decrypt(data)

        output_path.write_bytes(decrypted)