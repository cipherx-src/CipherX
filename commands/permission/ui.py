from assets.embeds import EmbedFactory
from assets.icons import Icons


class PermissionUI:
    """Builds the permission status embed."""

    @staticmethod
    def create_dashboard(permissions: dict):
        embed = EmbedFactory.primary(
            title=f"{Icons.PERMISSION} CipherX Permissions",
            description="Current permissions granted to CipherX in this server.",
        )

        def status(value: bool) -> str:
            return Icons.SUCCESS if value else Icons.ERROR

        embed.add_field(
            name="Required Permissions",
            value=(
                f"{status(permissions['send_messages'])} Send Messages\n"
                f"{status(permissions['embed_links'])} Embed Links\n"
                f"{status(permissions['attach_files'])} Attach Files\n"
                f"{status(permissions['manage_messages'])} Manage Messages\n"
                f"{status(permissions['administrator'])} Administrator"
            ),
            inline=False,
        )

        return embed