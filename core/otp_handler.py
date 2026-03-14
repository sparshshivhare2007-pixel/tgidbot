import re
import asyncio
from pyrogram import Client
from config import API_ID, API_HASH

async def get_telegram_otp(session_string):
    """Logs into a string session and fetches the latest OTP from Telegram"""
    try:
        async with Client(":memory:", session_string=session_string, api_id=API_ID, api_hash=API_HASH) as app:
            # Check last 3 messages from Telegram (ID 777000)
            async for message in app.get_chat_history(777000, limit=3):
                # Search for 5-digit code
                otp = re.search(r'\b(\d{5})\b', message.text)
                if otp:
                    return otp.group(1)
        return None
    except Exception:
        return "EXPIRED" # Session is dead or account is banned
