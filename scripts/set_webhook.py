from telegram import Update

import config
from ptb.tg_app import tg_app


async def set_webhook() -> bool:
    """Pass webhook settings to telegram"""
    await tg_app.bot.set_webhook(
        url=config.WEBHOOK_URL,
        allowed_updates=[Update.MESSAGE, Update.CALLBACK_QUERY],
        secret_token=config.SECRET_TOKEN,
    )
