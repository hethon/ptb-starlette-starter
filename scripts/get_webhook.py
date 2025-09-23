'''run this file to get information about webhook'''
import os
from telegram import Bot, WebhookInfo
from dotenv import load_dotenv


load_dotenv()


async def get_webhook() -> WebhookInfo:
    TOKEN = os.environ["BOT_TOKEN"]
    bot = Bot(TOKEN)
    async with bot:
        response = await bot.get_webhook_info()
        return response


if __name__ == "__main__":
    import asyncio
    result = asyncio.run(get_webhook())
    print(result)
