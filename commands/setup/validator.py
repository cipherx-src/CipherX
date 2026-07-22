import disnake


class SetupValidator:
    """Validation logic for the setup command."""

    @staticmethod
    def is_admin(inter: disnake.ApplicationCommandInteraction) -> bool:
        return inter.author.guild_permissions.administrator