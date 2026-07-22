import disnake

from app.bot import bot
from commands.file.service import FileService
from commands.file.ui import FileUI
from commands.file.validator import FileValidator


@bot.slash_command(
    name="file",
    description="Upload and validate a file."
)
async def file(
    inter: disnake.ApplicationCommandInteraction,
    attachment: disnake.Attachment,
):
    if not FileValidator.is_admin(inter):
        await inter.response.send_message(
            "❌ You must be an administrator to use this command.",
            ephemeral=True,
        )
        return

    try:
        file_path = await FileService.save_attachment(attachment)

        embed = FileUI.create_dashboard(file_path)

        await inter.response.send_message(embed=embed)

    except ValueError as e:
        await inter.response.send_message(
            f"❌ {e}",
            ephemeral=True,
        )