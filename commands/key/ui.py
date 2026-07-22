from assets.embeds import EmbedFactory
from assets.icons import Icons


class KeyUI:
    """Builds the key management embed."""

    @staticmethod
    def create_dashboard(created: bool):
        embed = EmbedFactory.primary(
            title=f"{Icons.KEY} CipherX Key Manager",
            description="Manage the encryption key for this server.",
        )

        if created:
            status = f"New encryption key generated {Icons.SUCCESS}"
        else:
            status = f"Encryption key is configured {Icons.SUCCESS}"

        embed.add_field(
            name="Key Status",
            value=status,
            inline=False,
        )

        return embed