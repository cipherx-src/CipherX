import disnake

from assets.icons import Icons
from commands.help.ui import HelpUI


class HomeButton(disnake.ui.Button):

    def __init__(self):
        super().__init__(
            label="Home",
            style=disnake.ButtonStyle.secondary,
            emoji=Icons.emoji(Icons.HOME),
        )

    async def callback(
        self,
        inter: disnake.MessageInteraction,
    ):
        await inter.response.edit_message(
            embed=HelpUI.home(),
            view=self.view,
        )