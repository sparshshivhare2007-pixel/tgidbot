from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from config import CHANNELS
from database.models import get_user
from utils.keyboards import main_menu_kb, must_join_kb

async def is_subscribed(user_id, context):
    """Check if user is in all required channels."""
    for channel in CHANNELS:
        try:
            member = await context.bot.get_chat_member(chat_id=channel, user_id=user_id)
            if member.status in ["left", "kicked"]:
                return False
        except Exception:
            return False
    return True

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    await get_user(user_id) # Ensure user exists in DB

    if not await is_subscribed(user_id, context):
        await update.message.reply_text(
            "❌ **Access Denied!**\n\nYou must join our channels to use this bot.",
            reply_markup=must_join_kb(),
            parse_mode="Markdown"
        )
        return

    await update.message.reply_text(
        f"👋 **Welcome to ID Provider Bot!**\n\nYour one-stop shop for Telegram accounts.",
        reply_markup=main_menu_kb(),
        parse_mode="Markdown"
    )
