from telegram import Update
from telegram.ext import ContextTypes
from database.models import get_user, get_available_countries
from utils.keyboards import countries_kb # You'll define this in utils

async def wallet(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    user = await get_user(query.from_user.id)
    
    text = (
        f"💳 **Your Wallet**\n\n"
        f"💰 Balance: `{user['balance']} INR`\n\n"
        "To recharge, scan the QR code below and send the screenshot."
    )
    # You can send a photo of your QR here
    await query.message.reply_photo(
        photo="YOUR_QR_IMAGE_URL_OR_FILE_ID",
        caption=text,
        parse_mode="Markdown"
    )

async def show_countries(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    countries = await get_available_countries()
    
    if not countries:
        await query.answer("😔 Out of stock!", show_alert=True)
        return

    await query.edit_message_text(
        "🌍 **Select a Country:**",
        reply_markup=countries_kb(countries),
        parse_mode="Markdown"
    )
