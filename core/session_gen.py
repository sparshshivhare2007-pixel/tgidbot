from pyrogram import Client
from config import API_ID, API_HASH

async def start_login(phone):
    """Starts the login process and returns phone_code_hash"""
    temp_client = Client(":memory:", api_id=API_ID, api_hash=API_HASH)
    await temp_client.connect()
    try:
        code_info = await temp_client.send_code(phone)
        return temp_client, code_info.phone_code_hash
    except Exception as e:
        await temp_client.disconnect()
        raise e

async def finish_login(client, phone, code_hash, otp, password=None):
    """Completes login and returns the String Session"""
    try:
        await client.sign_in(phone, code_hash, otp)
    except Exception: # Handles 2FA if enabled
        if password:
            await client.check_password(password)
        else:
            raise Exception("2FA_REQUIRED")

    session_string = await client.export_session_string()
    await client.disconnect()
    return session_string
