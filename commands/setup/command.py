import disnake

from app.bot import bot
from commands.setup.service import SetupService
from commands.setup.ui import SetupUI
from commands.setup.validator import SetupValidator
from commands.setup.view import SetupView


@bot.slash_command(
    name="setup",
    description="Display the CipherX setup dashboard."
)
async def setup(inter: disnake.ApplicationCommandInteraction):

    if not SetupValidator.is_admin(inter):
        await inter.response.send_message(
            "<:warning:1528084129986641981> You must be an administrator to use this command.",
            ephemeral=True,
        )
        return

    status = SetupService.get_status(inter.guild.id)

    embed = SetupUI.create_dashboard(status)

    view = SetupView(inter.guild.id)

    await inter.response.send_message(
        embed=embed,
        view=view,
        ephemeral=True,
    )

    view.message = await inter.original_response()