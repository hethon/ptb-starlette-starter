"""run this file to set about webhook url"""
from dotenv import load_dotenv
from telegram import Update

from config import config
from ptb.tg_app import tg_app

load_dotenv()


async def set_webhook() -> bool:
    """Pass webhook settings to telegram"""
    if not config.WEBHOOK_URL:
        raise Exception("WEBHOOK_URL is not set.") # noqa: TRY002

    return await tg_app.bot.set_webhook(
        url=config.WEBHOOK_URL,
        allowed_updates=[Update.MESSAGE, Update.CALLBACK_QUERY],
        secret_token=config.SECRET_TOKEN,
    )


if __name__ == "__main__":
    import asyncio
    result = asyncio.run(set_webhook())
    print(result)
