import disnake

from commands.key.service import KeyService
from commands.setup.buttons import (
    GenerateKeyButton,
    RotateKeyButton,
    PermissionButton,
    SettingsButton,
)


class SetupView(disnake.ui.View):

    def __init__(self, guild_id: int):
        super().__init__(timeout=300)

        self.guild_id = guild_id
        self.message: disnake.Message | None = None

        if KeyService.has_key(guild_id):
            self.add_item(RotateKeyButton())
        else:
            self.add_item(GenerateKeyButton())

        self.add_item(PermissionButton())
        self.add_item(SettingsButton())

    async def on_timeout(self):

        for item in self.children:
            item.disabled = True

        if self.message is None:
            return

        try:
            await self.message.edit(view=self)
        except disnake.HTTPException:
            pass