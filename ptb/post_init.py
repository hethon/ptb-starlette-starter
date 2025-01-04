from telegram.ext import Application


async def post_init(application: Application) -> None:
    """initialize things"""
    # for example you can set default values to bot_data
    # application.bot_data.setdefault("some_key", "some_value")
    return
