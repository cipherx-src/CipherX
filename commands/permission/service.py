import disnake


class PermissionService:
    """Business logic for the permission command."""

    @staticmethod
    def get_permissions(
        inter: disnake.ApplicationCommandInteraction,
    ) -> dict:

        bot_member = inter.guild.me

        permissions = bot_member.guild_permissions

        return {
            "send_messages": permissions.send_messages,
            "embed_links": permissions.embed_links,
            "attach_files": permissions.attach_files,
            "manage_messages": permissions.manage_messages,
            "administrator": permissions.administrator,
        }