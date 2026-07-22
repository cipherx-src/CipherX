import disnake

from app.bot import bot
from commands.settings.service import SettingsService
from commands.settings.ui import SettingsUI
from commands.settings.validator import SettingsValidator


@bot.slash_command(
    name="settings",
    description="View CipherX configuration settings."
)
async def settings(inter: disnake.ApplicationCommandInteraction):

    if not SettingsValidator.is_admin(inter):
        await inter.response.send_message(
            "❌ You must be an administrator to use this command.",
            ephemeral=True,
        )
        return

    config = SettingsService.get_settings()

    embed = SettingsUI.create_dashboard(config)

    await inter.response.send_message(embed=embed)