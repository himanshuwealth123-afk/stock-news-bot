import asyncio
from telegram import Bot
from telegram.error import TelegramError
import os
import time
import config

async def main():
    bot = Bot(token=config.BOT_TOKEN)
    test_text = """TEST MESSAGE FROM YOUR BOT 🚀
This is a test from Railway deployment.
If you see this → bot is live!"""

    for attempt in range(3):
        try:
            await bot.send_message(
                chat_id=config.CHANNEL_ID,
                text=test_text,
                parse_mode="HTML"
            )
            print("SUCCESS: Test message sent!")
            break
        except TelegramError as e:
            print(f"Telegram error (attempt {attempt+1}): {e}")
            break
        except Exception as e:
            print(f"Retry error (attempt {attempt+1}): {e}")
            time.sleep(10)

if __name__ == "__main__":
    asyncio.run(main())
