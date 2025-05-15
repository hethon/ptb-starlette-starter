from telegram.ext import (
    Application,
    CallbackContext,
    ExtBot,
)

from .custom_updates import CustomUpdate


class CustomContext(CallbackContext[ExtBot, dict, dict, dict]):
    """
    Custom CallbackContext class that makes `user_data` available for updates of type
    `CustomUpdate`.
    """

    @classmethod
    def from_update(
        cls,
        update: object,
        application: "Application",
    ) -> "CustomContext":
        if isinstance(update, CustomUpdate):
            return cls(application=application, user_id=update.user_id)
        return super().from_update(update, application)
