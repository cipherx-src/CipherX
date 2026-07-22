import disnake

from app.bot import bot
from commands.permission.service import PermissionService
from commands.permission.ui import PermissionUI
from commands.permission.validator import PermissionValidator


@bot.slash_command(
    name="permission",
    description="Check CipherX permissions in this server."
)
async def permission(inter: disnake.ApplicationCommandInteraction):

    if not PermissionValidator.is_admin(inter):
        await inter.response.send_message(
            "❌ You must be an administrator to use this command.",
            ephemeral=True,
        )
        return

    permissions = PermissionService.get_permissions(inter)

    embed = PermissionUI.create_dashboard(permissions)

    await inter.response.send_message(embed=embed)