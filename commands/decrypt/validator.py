import disnake


class DecryptValidator:
    @staticmethod
    def is_admin(inter: disnake.ApplicationCommandInteraction) -> bool:
        return inter.author.guild_permissions.administrator