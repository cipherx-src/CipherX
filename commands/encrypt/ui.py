from assets.embeds import EmbedFactory
from assets.icons import Icons


class EncryptUI:
    @staticmethod
    def success(file_name: str):
        embed = EmbedFactory.primary(
            title=f"{Icons.ENCRYPT} Encryption Complete",
            description="The file has been encrypted successfully.",
        )

        embed.add_field(
            name="Output File",
            value=f"`{file_name}`",
            inline=False,
        )

        return embed