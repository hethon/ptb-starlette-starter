from typing import cast

from telegram import Message, Update, User

from config.locale import Locale

from .custom_context import CustomContext
from .custom_updates import CustomUpdate
from persistence.db import Session
from persistence.models import User as DBUser


async def start(update: Update, context: CustomContext) -> None:
    """Display a welcome message."""
    user = cast(User, update.effective_user)
    user_id = user.id
    name = user.full_name
    username = user.username
    
    async with Session() as session:
        async with session.begin():
            user = await session.get(DBUser, user_id)
            if not user:
                session.add(DBUser(tg_id=user_id, tg_name=name, tg_username=username))

    await cast(Message, update.message).reply_html(
        text=Locale.get("welcome_message", lang="en", full_name=name)
    )


async def custom_update(update: CustomUpdate, context: CustomContext) -> None:
    """Handle custom updates."""
    user_id = update.user_id
    payload = update.payload

    # context.user_data gives the data related to user_id
    # do anything you want with user_id and payload

    await context.bot.send_message(chat_id=user_id, text=payload)
