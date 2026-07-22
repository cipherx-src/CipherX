import disnake

from assets.colors import Colors
from assets.icons import Icons


class EmbedFactory:
    """Factory class for creating consistent embeds."""

    @staticmethod
    def create(
        title: str,
        description: str | None = None,
        color: disnake.Color = Colors.PRIMARY,
    ) -> disnake.Embed:
        embed = disnake.Embed(
            title=title,
            description=description,
            color=color,
        )

        embed.timestamp = disnake.utils.utcnow()

        embed.set_footer(
            text="CipherX • Secure Encryption",
            icon_url=None,
        )

        return embed

    @staticmethod
    def primary(
        title: str,
        description: str | None = None,
    ):
        return EmbedFactory.create(
            title,
            description,
            Colors.PRIMARY,
        )

    @staticmethod
    def success(
        title: str,
        description: str | None = None,
    ):
        return EmbedFactory.create(
            title,
            description,
            Colors.SUCCESS,
        )

    @staticmethod
    def warning(
        title: str,
        description: str | None = None,
    ):
        return EmbedFactory.create(
            title,
            description,
            Colors.WARNING,
        )

    @staticmethod
    def error(
        title: str,
        description: str | None = None,
    ):
        return EmbedFactory.create(
            title,
            description,
            Colors.ERROR,
        )

    @staticmethod
    def info(
        title: str,
        description: str | None = None,
    ):
        return EmbedFactory.create(
            title,
            description,
            Colors.INFO,
        )