from app.bot import bot
from services.logging.logger import setup_logger

logger = setup_logger()


@bot.event
async def on_ready():
    logger.info(f"CipherX is online as {bot.user}")