import disnake

from app.bot import bot
from commands.key.service import KeyService
from commands.key.ui import KeyUI
from commands.key.validator import KeyValidator


@bot.slash_command(
    name="key",
    description="Manage the encryption key for this server."
)
async def key(inter: disnake.ApplicationCommandInteraction):

    if not KeyValidator.is_admin(inter):
        await inter.response.send_message(
            "<:warning:1528084129986641981> You must be an administrator to use this command.",
            ephemeral=True,
        )
        return

    guild_id = inter.guild.id

    created, _ = KeyService.ensure_key(guild_id)

    embed = KeyUI.create_dashboard(created)

    await inter.response.send_message(embed=embed)