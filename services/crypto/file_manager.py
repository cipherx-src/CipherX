from pathlib import Path


class FileManager:
    @staticmethod
    def ensure_dir(path: Path):
        path.mkdir(parents=True, exist_ok=True)

    @staticmethod
    def delete(path: Path):
        if path.exists():
            path.unlink()

    @staticmethod
    def cleanup(*paths: Path):
        for path in paths:
            FileManager.delete(path)