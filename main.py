import os
from dotenv import load_dotenv
import httpx
from pyrogram import filters
from pyrogram.client import Client
from pyrogram.types import Message

load_dotenv(".env")
api_id = os.getenv("API_KEY")
api_hash = os.getenv("API_HASH")
DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")
app = Client("my_account", api_id, api_hash)

@app.on_message(filters.chat("haveloc_notifier_bot")) 
async def monitorMessage(client: Client, message: Message):
    if message.text:
        print(f"[MSG] Message Recieved: {message.text}")
        await send_to_discord(message.text)

def truncate_message(text: str, max_len: int)-> str:
    if len(text) > max_len:
        return text[:max_len] + "\n ... (truncated)"
    return text

async def send_to_discord(content: str):
    truncated = truncate_message(content, 1900)
    async with httpx.AsyncClient() as client:
        json_data = {"content": truncated}
        response = await client.post(DISCORD_WEBHOOK_URL, json=json_data)
        if response.status_code != 204:
            print("[ERR] Failed to send Discord Webhook")

print("[INFO] Bot Started Successfully")
app.run()


