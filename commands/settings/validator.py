import disnake


class SettingsValidator:
    """Validation logic for the settings command."""

    @staticmethod
    def is_admin(inter: disnake.ApplicationCommandInteraction) -> bool:
        return inter.author.guild_permissions.administrator