# Haveloc Discord Notifier

## Requirements:

- Telegram Haveloc Notifier Enabled [Haveloc Notifier Registration](https://app.haveloc.com/notifications)
- Telegram Number
- Telegram API and HASH
- Discord Webhook URL
- Python and pip

## Usage:

1. Get api token and hash from [here](https://my.telegram.org)
2. Create a Discord Webhook inside your Discord Server Channel

- Channel settings > Integrations > Webhook > Create New Webhook > Copy Webhook

3. Move `.env.example` to `.env`
4. Populate `.env` with the above 3 values
5. Install requirements from requirements.txt using `pip install -r requirements.txt`
6. Start the bot using `python main.py`
7. On first launch it will prompt for phone number (Enter phone number with country code)
8. Profit

## Testing:
To Test the Working of the script and not wait for an actual notification,
You can dm the haveloc notifier and it should send a webhook with your message
