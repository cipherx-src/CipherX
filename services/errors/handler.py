import disnake

from assets.embeds import EmbedFactory
from assets.icons import Icons
from services.logging.action_logger import ActionLogger


class ErrorHandler:

    @staticmethod
    async def handle(
        inter: disnake.ApplicationCommandInteraction,
        error: Exception,
    ):
        ActionLogger.error(str(error))

        embed = EmbedFactory.error(
            title=f"{Icons.ERROR} Error",
            description=str(error),
        )

        if inter.response.is_done():
            await inter.followup.send(
                embed=embed,
                ephemeral=True,
            )
        else:
            await inter.response.send_message(
                embed=embed,
                ephemeral=True,
            )