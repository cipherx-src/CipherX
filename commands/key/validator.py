import disnake


class KeyValidator:
    """Validation logic for the key command."""

    @staticmethod
    def is_admin(inter: disnake.ApplicationCommandInteraction) -> bool:
        return inter.author.guild_permissions.administrator