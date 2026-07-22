from assets.embeds import EmbedFactory
from assets.icons import Icons


class DecryptUI:
    @staticmethod
    def success(file_name: str):
        embed = EmbedFactory.primary(
            title=f"{Icons.DECRYPT} Decryption Complete",
            description="The file has been decrypted successfully.",
        )

        embed.add_field(
            name="Output File",
            value=f"`{file_name}`",
            inline=False,
        )

        return embed