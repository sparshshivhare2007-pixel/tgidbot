from motor.motor_asyncio import AsyncIOMotorClient
from config import MONGO_URI

# Initialize MongoDB Client
client = AsyncIOMotorClient(MONGO_URI)
db = client.id_provider_db

# Collections
users_db = db.users          # Stores user ID, balance, etc.
accounts_db = db.accounts    # Stores available Telegram IDs & sessions
recharges_db = db.recharges  # Stores pending/approved payment screenshots
