import os
import importlib


class CommandLoader:

    def __init__(self, bot):
        self.bot = bot
        self.commands_path = "commands"

    async def load_commands(self):
        for folder in os.listdir(self.commands_path):

            folder_path = os.path.join(
                self.commands_path,
                folder
            )

            if not os.path.isdir(folder_path):
                continue

            try:
                module = importlib.import_module(
                    f"{self.commands_path}.{folder}.command"
                )

                if hasattr(module, "setup"):
                    await module.setup(self.bot)

                print(f"[LOADER] Loaded command: {folder}")

            except Exception as e:
                print(
                    f"[LOADER ERROR] {folder}: {e}"
                )