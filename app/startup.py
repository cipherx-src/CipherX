from app.bot import bot, TOKEN
from services.discord.command_loader import load_commands
from services.logging.logger import setup_logger

logger = setup_logger()


def run():
    logger.info("Loading commands...")
    load_commands()

    logger.info("Starting CipherX...")
    bot.run(TOKEN)