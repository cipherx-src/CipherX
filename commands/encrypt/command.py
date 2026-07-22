from assets.icons import Icons
import disnake

from app.bot import bot
from assets.icons import Icons
from commands.encrypt.service import EncryptService
from commands.encrypt.ui import EncryptUI
from commands.encrypt.validator import EncryptValidator
from commands.file.service import FileService
from services.crypto.file_manager import FileManager
from services.errors.handler import ErrorHandler

@bot.slash_command(
    name="encrypt",
    description="Encrypt a file."
)
async def encrypt(
    inter: disnake.ApplicationCommandInteraction,
    attachment: disnake.Attachment,
):
    if not EncryptValidator.is_admin(inter):
        await inter.response.send_message(
            f"{Icons.ERROR} You must be an administrator to use this command.",
            ephemeral=True,
        )
        return

    try:
        input_path = await FileService.save_encrypt_attachment(
            attachment
        )

        output_path = EncryptService.encrypt(
            guild_id=inter.guild.id,
            input_path=input_path,
        )

        embed = EncryptUI.success(
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