import os
import requests
from dotenv import load_dotenv

load_dotenv()  # loads .env file

TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")


def send_telegram(message):
    """Send a message to your Telegram using your bot."""
    if not TOKEN or not CHAT_ID:
        print("⚠️ Telegram credentials missing in .env file")
        return

    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    try:
        requests.post(url, data={"chat_id": CHAT_ID, "text": message})
    except Exception as e:
        print("⚠️ Failed to send Telegram message:", e)
