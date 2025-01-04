from telegram.ext import (
    ApplicationBuilder,
    ContextTypes,
    Defaults,
    PicklePersistence,
    PersistenceInput,
    CommandHandler,
    TypeHandler,
)
from telegram.constants import ParseMode

import config.config as config
from .custom_context import CustomContext
from .custom_updates import CustomUpdate
from .handlers import start, custom_update
from .error_handler import report_error


context_types = ContextTypes(context=CustomContext)
defaults = Defaults(parse_mode=ParseMode.HTML, allow_sending_without_reply=True)
persistence = PicklePersistence(
    "persistence/persistence.pkl", PersistenceInput(chat_data=False, callback_data=False)
)
tg_app_builder = (
    ApplicationBuilder()
    .token(config.BOT_TOKEN)
    .context_types(context_types)
    .defaults(defaults)
    .persistence(persistence)
)

if config.MODE == config.Mode.webhook:
    # Here we set updater to None because we want our custom webhook server to handle the updates
    # and hence we don't need an Updater instance
    tg_app_builder = tg_app_builder.updater(None).build()


tg_app = tg_app_builder.build()

tg_app.add_handler(CommandHandler("start", start))
tg_app.add_handler(TypeHandler(type=CustomUpdate, callback=custom_update))
tg_app.add_error_handler(report_error)
