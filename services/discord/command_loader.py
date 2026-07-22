import importlib
from pathlib import Path


def load_commands():
    commands_dir = Path("commands")

    for folder in commands_dir.iterdir():
        if not folder.is_dir():
            continue

        command_file = folder / "command.py"

        if command_file.exists():
            importlib.import_module(
                f"commands.{folder.name}.command"
            )
            print(f"[COMMAND LOADED] {folder.name}")