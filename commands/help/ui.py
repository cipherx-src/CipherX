from assets.embeds import EmbedFactory
from assets.icons import Icons


class HelpUI:

    @staticmethod
    def home():
        embed = EmbedFactory.primary(
            title=f"{Icons.HELP} CipherX Help",
            description=(
                "Welcome to **CipherX**.\n\n"
                "Select a category from the dropdown below "
                "to view available commands."
            ),
        )

        return embed

    @staticmethod
    def encryption():
        embed = EmbedFactory.primary(
            title=f"{Icons.ENCRYPT} Encryption Commands",
        )

        embed.add_field(
            name=f"{Icons.KEY} /key",
            value="Manage encryption keys.",
            inline=False,
        )

        embed.add_field(
            name=f"{Icons.ENCRYPT} /encrypt",
            value="Encrypt a file.",
            inline=False,
        )

        embed.add_field(
            name=f"{Icons.DECRYPT} /decrypt",
            value="Decrypt a file.",
            inline=False,
        )

        return embed

    @staticmethod
    def configuration():
        embed = EmbedFactory.primary(
            title=f"{Icons.SETTINGS} Configuration",
        )

        embed.add_field(
            name=f"{Icons.SETUP} /setup",
            value="Configure CipherX.",
            inline=False,
        )

        embed.add_field(
            name=f"{Icons.PERMISSION} /permission",
            value="Check bot permissions.",
            inline=False,
        )

        embed.add_field(
            name=f"{Icons.SETTINGS} /settings",
            value="View current settings.",
            inline=False,
        )

        return embed

    @staticmethod
    def utilities():
        embed = EmbedFactory.primary(
            title=f"{Icons.FILE} Utilities",
        )

        embed.add_field(
            name="🏓 /ping",
            value="Check bot latency.",
            inline=False,
        )

        embed.add_field(
            name=f"{Icons.HELP} /help",
            value="Show the help menu.",
            inline=False,
        )

        return embed