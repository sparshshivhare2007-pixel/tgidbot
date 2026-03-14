from telegram import Update
from telegram.ext import ContextTypes, ConversationHandler, MessageHandler, filters
from config import ADMIN_ID
from database.models import update_balance

# States for Adding ID Conversation
PHONE, OTP, PASS, PRICE = range(4)

async def approve_recharge(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Callback for 'Approve' button on a screenshot."""
    query = update.callback_query
    if query.from_user.id != ADMIN_ID: return

    # Data format: "approve:USERID:AMOUNT"
    _, user_id, amount = query.data.split(":")
    
    await update_balance(int(user_id), float(amount))
    await query.message.edit_caption(f"✅ Approved {amount} INR for user {user_id}")
    
    # Notify user
    await context.bot.send_message(
        chat_id=user_id, 
        text=f"✅ Your recharge of {amount} INR has been approved!"
    )

# --- ID Adding Flow (Logic overview) ---
# You would use a ConversationHandler here to:
# 1. Ask for phone
# 2. Trigger Pyrogram to send OTP
# 3. Ask for OTP
# 4. Save session to MongoDB using 'add_new_account' from models.py
