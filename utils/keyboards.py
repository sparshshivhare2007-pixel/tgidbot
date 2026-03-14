from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def main_menu_kb():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🛒 Buy Account", callback_data="buy_menu")],
        [InlineKeyboardButton("💰 Wallet", callback_data="wallet"), 
         InlineKeyboardButton("👤 Profile", callback_data="profile")]
    ])

def must_join_kb():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("Join Channel 1", url="https://t.me/yourch1")],
        [InlineKeyboardButton("Join Channel 2", url="https://t.me/yourch2")],
        [InlineKeyboardButton("✅ Joined", callback_data="check_joined")]
    ])

def countries_kb(countries_list):
    """Generates buttons for each country that has stock"""
    keyboard = []
    for country in countries_list:
        keyboard.append([InlineKeyboardButton(f"🌍 {country}", callback_data=f"country:{country}")])
    keyboard.append([InlineKeyboardButton("⬅️ Back", callback_data="main_menu")])
    return InlineKeyboardMarkup(keyboard)

def admin_approval_kb(user_id, amount):
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("✅ Approve", callback_data=f"approve:{user_id}:{amount}"),
         InlineKeyboardButton("❌ Reject", callback_data=f"reject:{user_id}")]
    ])
