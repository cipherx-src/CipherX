from assets.icons import Icons
import disnake

from app.bot import bot
from assets.icons import Icons
from commands.decrypt.service import DecryptService
from commands.decrypt.ui import DecryptUI
from commands.decrypt.validator import DecryptValidator
from commands.file.service import FileService
from services.crypto.file_manager import FileManager
from services.errors.handler import ErrorHandler

@bot.slash_command(
    name="decrypt",
    description="Decrypt a file."
)
async def decrypt(
    inter: disnake.ApplicationCommandInteraction,
    attachment: disnake.Attachment,
):
    if not DecryptValidator.is_admin(inter):
        await inter.response.send_message(
            f"{Icons.ERROR} You must be an administrator to use this command.",
            ephemeral=True,
        )
        return

    try:
        input_path = await FileService.save_decrypt_attachment(
            attachment
        )

        output_path = DecryptService.decrypt(
            guild_id=inter.guild.id,
            input_path=input_path,
        )

        embed = DecryptUI.success(
            output_path.name
        )

        await inter.response.send_message(
            embed=embed,
            file=disnake.File(output_path),
        )

        FileManager.cleanup(
            input_path,
            output_path,
        )

    except Exception as e:
        await ErrorHandler.handle(inter, e)