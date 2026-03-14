from database.db_client import users_db, accounts_db, recharges_db
from datetime import datetime

# --- USER FUNCTIONS ---

async def get_user(user_id: int):
    """Fetch user data or create a new user profile."""
    user = await users_db.find_one({"user_id": user_id})
    if not user:
        user = {
            "user_id": user_id,
            "balance": 0.0,
            "joined_at": datetime.utcnow(),
            "total_spent": 0.0
        }
        await users_db.insert_one(user)
    return user

async def update_balance(user_id: int, amount: float):
    """Add or subtract balance from a user."""
    await users_db.update_one(
        {"user_id": user_id},
        {"$inc": {"balance": amount}},
        upsert=True
    )

# --- ACCOUNT FUNCTIONS ---

async def add_new_account(phone, country, session_string, price, password=None):
    """Admin uses this to add a new ID to the stock."""
    account = {
        "phone": phone,
        "country": country.upper(),
        "session": session_string,
        "price": price,
        "two_step": password,
        "is_sold": False,
        "added_at": datetime.utcnow(),
        "buyer_id": None
    }
    return await accounts_db.insert_one(account)

async def get_available_countries():
    """Returns a list of unique countries that have unsold accounts."""
    return await accounts_db.distinct("country", {"is_sold": False})

async def get_stock_by_country(country: str):
    """Get list of unsold accounts for a specific country."""
    cursor = accounts_db.find({"country": country.upper(), "is_sold": False})
    return await cursor.to_list(length=100)

# --- TRANSACTION FUNCTIONS ---

async def log_recharge_request(user_id, file_id, amount=0):
    """Save the screenshot sent by the user for admin approval."""
    request = {
        "user_id": user_id,
        "file_id": file_id,
        "status": "pending",
        "timestamp": datetime.utcnow()
    }
    result = await recharges_db.insert_one(request)
    return result.inserted_id
