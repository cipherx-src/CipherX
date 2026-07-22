from app.bot import bot

from commands.help.ui import HelpUI
from commands.help.view import HelpView


@bot.slash_command(
    name="help",
    description="Show the help menu.",
)
async def help(inter):

    view = HelpView()

    await inter.response.send_message(
        embed=HelpUI.home(),
        view=view,
        ephemeral=False,
    )

    view.message = await inter.original_response()