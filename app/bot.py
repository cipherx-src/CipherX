import os

import disnake
from disnake.ext import commands
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")

intents = disnake.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.InteractionBot(
    intents=intents,
)