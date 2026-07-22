from assets.embeds import EmbedFactory
from assets.icons import Icons


class SetupUI:
    """Builds the setup dashboard embed."""

    @staticmethod
    def create_dashboard(status: dict):
        embed = EmbedFactory.primary(
            title=f"{Icons.SETUP} CipherX Setup",
            description="Configure and manage CipherX for this server.",
        )

        embed.add_field(
    name="System Status",
    value=(
        f"{Icons.KEY} Key: "
        f"{Icons.SUCCESS if status['key'] else Icons.ERROR}\n"

        f"{Icons.PERMISSION} Permission: "
        f"{Icons.SUCCESS if status['permission'] else Icons.ERROR}\n"

        f"{Icons.SETTINGS} Settings: "
        f"{Icons.SUCCESS if status['settings'] else Icons.ERROR}"
    ),
    inline=False,
)

        return embed