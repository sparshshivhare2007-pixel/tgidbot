from handlers.user import wallet, show_countries
from handlers.admin import approve_recharge

async def handle_callbacks(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    data = query.data

    if data == "wallet":
        await wallet(update, context)
    elif data == "buy_menu":
        await show_countries(update, context)
    elif data.startswith("approve:"):
        await approve_recharge(update, context)
    # Add logic for "check_joined", "select_country", "buy_account", "get_otp"
