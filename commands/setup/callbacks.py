import disnake

from commands.setup.service import SetupService
from commands.setup.ui import SetupUI


class SetupCallbacks:

    @staticmethod
    async def generate_key(
        inter: disnake.MessageInteraction,
        view,
    ):
        status = SetupService.get_status()

        embed = SetupUI.create_dashboard(status)

        await inter.response.edit_message(
            embed=embed,
            view=view,
        )

    @staticmethod
    async def permission(
        inter: disnake.MessageInteraction,
        view,
    ):
        status = SetupService.get_status()

        embed = SetupUI.create_dashboard(status)

        await inter.response.edit_message(
            embed=embed,
            view=view,
        )

    @staticmethod
    async def settings(
        inter: disnake.MessageInteraction,
        view,
    ):
        status = SetupService.get_status()

        embed = SetupUI.create_dashboard(status)

        await inter.response.edit_message(
            embed=embed,
            view=view,
        )