from app.bot import bot


@bot.slash_command(
    name="ping",
    description="Check bot latency"
)
async def ping(inter):
    await inter.response.send_message("🏓 Pong!")