from assets.embeds import EmbedFactory
from assets.icons import Icons


class SettingsUI:
    """Builds the settings embed."""

    @staticmethod
    def create_dashboard(settings: dict):

        embed = EmbedFactory.primary(
            title=f"{Icons.SETTINGS} CipherX Settings",
            description="Current CipherX configuration.",
        )

        if not settings:
            embed.add_field(
                name="Configuration",
                value="⚠️ No configuration found.",
                inline=False,
            )
            return embed

        config_text = "\n".join(
            [
                f"🔹 **{key}**: `{value}`"
                for key, value in settings.items()
            ]
        )

        embed.add_field(
            name="Configuration",
            value=config_text,
            inline=False,
        )

        return embed