import disnake

from assets.icons import Icons
from commands.key.service import KeyService
from commands.setup.service import SetupService
from commands.setup.ui import SetupUI
from commands.permission.service import PermissionService
from commands.permission.ui import PermissionUI
from commands.settings.service import SettingsService
from commands.settings.ui import SettingsUI

class GenerateKeyButton(disnake.ui.Button):

    def __init__(self):
        super().__init__(
            label="Generate Key",
            style=disnake.ButtonStyle.primary,
            emoji=Icons.emoji(Icons.KEY),
            custom_id="setup_generate_key",
        )

    async def callback(
        self,
        inter: disnake.MessageInteraction,
    ):
        KeyService.ensure_key(inter.guild.id)

        status = SetupService.get_status(inter.guild.id)
        embed = SetupUI.create_dashboard(status)

        view = self.view.__class__(inter.guild.id)
        view.message = self.view.message

        await inter.response.edit_message(
    embed=embed,
    view=view,
)

class RotateKeyButton(disnake.ui.Button):
    
    def __init__(self):
        super().__init__(
            label="Rotate Key",
            style=disnake.ButtonStyle.danger,
            emoji=Icons.emoji(Icons.ROTATE),
            custom_id="setup_rotate_key",
        )

    async def callback(
        self,
        inter: disnake.MessageInteraction,
    ):
        KeyService.rotate_key(inter.guild.id)

        status = SetupService.get_status(inter.guild.id)

        embed = SetupUI.create_dashboard(status)

        view = self.view.__class__(inter.guild.id)
        view.message = self.view.message

        await inter.response.edit_message(
            embed=embed,
            view=view,
        )

class PermissionButton(disnake.ui.Button):
    
    def __init__(self):
        super().__init__(
            label="Permissions",
            style=disnake.ButtonStyle.secondary,
            emoji=Icons.emoji(Icons.PERMISSION),
            custom_id="setup_permission",
        )

    async def callback(
        self,
        inter: disnake.MessageInteraction,
    ):
        permissions = PermissionService.get_permissions(inter)

        embed = PermissionUI.create_dashboard(permissions)

        await inter.response.send_message(
            embed=embed,
            ephemeral=True,
        )

class SettingsButton(disnake.ui.Button):
    
    def __init__(self):
        super().__init__(
            label="Settings",
            style=disnake.ButtonStyle.secondary,
            emoji=Icons.emoji(Icons.SETTINGS),
            custom_id="setup_settings",
        )

    async def callback(
        self,
        inter: disnake.MessageInteraction,
    ):
        settings = SettingsService.get_settings()

        embed = SettingsUI.create_dashboard(settings)

        await inter.response.send_message(
            embed=embed,
            ephemeral=True,
        )