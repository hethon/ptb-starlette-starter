from telegram import Update

from config.locale import Locale

from .custom_context import CustomContext
from .custom_updates import CustomUpdate


async def start(update: Update, context: CustomContext) -> None:
    """Display a welcome message."""
    full_name = update.effective_user.full_name
    await update.message.reply_html(
        text=Locale.get("welcome_message", full_name=full_name)
    )


async def custom_update(update: CustomUpdate, context: CustomContext) -> None:
    """Handle custom updates."""
    user_id = update.user_id
    payload = update.payload

    # context.user_data gives the data related to user_id
    # do anything you want with user_id and payload

    await context.bot.send_message(chat_id=user_id, text=payload)
