"""
Run this once on your machine to authenticate Telethon.
It creates userbot.session, then the bot uses it automatically.

Usage: python auth_userbot.py
"""
import asyncio
import os
from dotenv import load_dotenv

load_dotenv()

API_ID = int(os.getenv("TELEGRAM_API_ID", "0"))
API_HASH = os.getenv("TELEGRAM_API_HASH", "")
PHONE = os.getenv("TELEGRAM_PHONE", "")
PASSWORD = os.getenv("TELEGRAM_2FA_PASSWORD", "")


async def main():
    from telethon import TelegramClient
    from telethon.errors import SessionPasswordNeededError

    if not API_ID or not API_HASH:
        print("❌ Missing TELEGRAM_API_ID or TELEGRAM_API_HASH in .env")
        return

    phone = PHONE or input("Enter your phone number (e.g. +972501234567): ").strip()

    print(f"\nConnecting to Telegram as {phone}...")
    client = TelegramClient("userbot", API_ID, API_HASH)
    await client.connect()

    if await client.is_user_authorized():
        me = await client.get_me()
        print(f"✅ Already logged in as {me.first_name}!")
        await client.disconnect()
        return

    await client.send_code_request(phone)
    code = input("Enter the code you received on Telegram: ").strip()

    try:
        await client.sign_in(phone=phone, code=code)
    except SessionPasswordNeededError:
        pwd = PASSWORD or input("Enter your 2FA password: ").strip()
        await client.sign_in(password=pwd)

    me = await client.get_me()
    print(f"\n✅ Successfully logged in as {me.first_name}!")
    print("✅ userbot.session file created.")
    print("You can now run: python bot.py")
    await client.disconnect()


if __name__ == "__main__":
    asyncio.run(main())
