from assets.embeds import EmbedFactory
from assets.icons import Icons


class FileUI:
    @staticmethod
    def create_dashboard(file_path):
        embed = EmbedFactory.primary(
            title=f"{Icons.FILE} File Manager",
            description="File received successfully.",
        )

        embed.add_field(
            name="File",
            value=f"`{file_path.name}`",
            inline=False,
        )

        embed.add_field(
            name="Location",
            value=f"`{file_path}`",
            inline=False,
        )

        return embed