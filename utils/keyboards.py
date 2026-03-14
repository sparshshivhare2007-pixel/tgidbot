from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def main_menu_kb():
    keyboard = [
        [InlineKeyboardButton("🛒 Buy Account", callback_data="buy_menu")],
        [InlineKeyboardButton("💰 Wallet", callback_data="wallet"), 
         InlineKeyboardButton("👤 Profile", callback_data="profile")],
        [InlineKeyboardButton("📢 Support", url="https://t.me/your_username")]
    ]
    return InlineKeyboardMarkup(keyboard)

def must_join_kb():
    keyboard = [
        [InlineKeyboardButton("Join Channel 1", url="https://t.me/channel1")],
        [InlineKeyboardButton("Join Channel 2", url="https://t.me/channel2")],
        [InlineKeyboardButton("✅ Joined", callback_data="check_joined")]
    ]
    return InlineKeyboardMarkup(keyboard)
