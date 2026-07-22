import disnake

from app.bot import bot
from commands.faq.service import FAQService
from commands.faq.ui import FAQUI


@bot.slash_command(
    name="faq",
    description="Display the CipherX FAQ dashboard."
)
async def faq(inter: disnake.ApplicationCommandInteraction):
    faqs = FAQService.get_questions()

    embed = FAQUI.create_dashboard(faqs)

    await inter.response.send_message(
        embed=embed,
        ephemeral=False,
    )