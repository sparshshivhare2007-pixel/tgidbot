from motor.motor_asyncio import AsyncIOMotorClient
from config import MONGO_URI

client = AsyncIOMotorClient(MONGO_URI)
db = client.id_provider_bot

# Collections
users_db = db.users
accounts_db = db.accounts
recharge_db = db.recharges
