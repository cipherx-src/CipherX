import disnake

from assets.icons import Icons
from commands.help.ui import HelpUI
from commands.help.buttons import HomeButton


class HelpSelect(disnake.ui.StringSelect):

    def __init__(self):
        super().__init__(
            placeholder="Select a category...",
            min_values=1,
            max_values=1,
            options=[
                disnake.SelectOption(
                    label="Encryption",
                    description="Encryption commands",
                    emoji=Icons.emoji(Icons.ENCRYPT),
                    value="encryption",
                ),
                disnake.SelectOption(
                    label="Configuration",
                    description="Configuration commands",
                    emoji=Icons.emoji(Icons.SETUP),
                    value="configuration",
                ),
                disnake.SelectOption(
                    label="Utilities",
                    description="Utility commands",
                    emoji=Icons.emoji(Icons.FILE),
                    value="utilities",
                ),
            ],
        )

    async def callback(
        self,
        inter: disnake.MessageInteraction,
    ):
        value = self.values[0]

        if value == "encryption":
            embed = HelpUI.encryption()

        elif value == "configuration":
            embed = HelpUI.configuration()

        else:
            embed = HelpUI.utilities()

        await inter.response.edit_message(
            embed=embed,
            view=self.view,
        )


class HelpView(disnake.ui.View):

    def __init__(self):
        super().__init__(timeout=300)

        self.message: disnake.Message | None = None

        self.add_item(HelpSelect())
        self.add_item(HomeButton())

    async def on_timeout(self):

        for item in self.children:
            item.disabled = True

        if self.message is None:
            return

        try:
            await self.message.edit(view=self)
        except disnake.HTTPException:
            pass