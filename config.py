import os
from dotenv import load_dotenv

load_dotenv()

# API Credentials from my.telegram.org
API_ID = int(os.getenv("API_ID", "0"))
API_HASH = os.getenv("API_HASH", "")

# Bot Credentials from @BotFather
BOT_TOKEN = os.getenv("BOT_TOKEN", "")
ADMIN_ID = int(os.getenv("ADMIN_ID", "0"))

# Database & Channels
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
CHANNELS = ["@Channel1", "@Channel2"]  # Replace with your channel usernames
