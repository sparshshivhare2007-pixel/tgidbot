import logging
from telegram import Update
from telegram.ext import (
    ApplicationBuilder, 
    CommandHandler, 
    CallbackQueryHandler, 
    MessageHandler, 
    ConversationHandler, 
    filters
)

from config import BOT_TOKEN, ADMIN_ID
from handlers.start import start
from handlers.callback_query import handle_callbacks
from handlers.admin import (
    add_id_start, 
    get_phone, 
    get_otp, 
    get_pass, 
    get_price, 
    cancel,
    PHONE, OTP, PASS, PRICE
)

# Enable Logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', 
    level=logging.INFO
)

def main():
    # Build the Application
    application = ApplicationBuilder().token(BOT_TOKEN).build()

    # 1. Admin /add Conversation Handler
    # This handles the step-by-step process of logging in an ID
    add_id_conv = ConversationHandler(
        entry_points=[CommandHandler("add", add_id_start, filters=filters.User(ADMIN_ID))],
        states={
            PHONE: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_phone)],
            OTP:   [MessageHandler(filters.TEXT & ~filters.COMMAND, get_otp)],
            PASS:  [MessageHandler(filters.TEXT & ~filters.COMMAND, get_pass)],
            PRICE: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_price)],
        },
        fallbacks=[CommandHandler("cancel", cancel)],
    )

    # 2. Main Command Handlers
    application.add_handler(CommandHandler("start", start))
    
    # 3. Conversation Handler (must be added before general CallbackQueryHandler)
    application.add_handler(add_id_conv)

    # 4. Global Callback Query Handler
    # This handles all button clicks: Wallet, Buy, Countries, OTP fetching, etc.
    application.add_handler(CallbackQueryHandler(handle_callbacks))

    # 5. Handle Screenshot Uploads (For Balance Recharge)
    # Filter for photos sent by users that are NOT the admin
    application.add_handler(MessageHandler(
        filters.PHOTO & ~filters.User(ADMIN_ID), 
        # You would point this to a function in handlers/user.py like 'handle_screenshot'
    ))

    print("---------------------------------------")
    print("🚀 ID Provider Bot is now LIVE!")
    print("---------------------------------------")
    
    application.run_polling()

if __name__ == '__main__':
    main()
