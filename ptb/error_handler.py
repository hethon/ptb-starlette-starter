from telegram import Update

from .custom_context import CustomContext
from config.config import DEV_USER_ID


async def report_error(update: Update, context: CustomContext) -> None:
    """Report an error to the developer"""

    exception = context.error

    trace = []
    tb = exception.__traceback__
    while tb is not None:
        trace.append(
            {
                "filename": tb.tb_frame.f_code.co_filename,
                "name": tb.tb_frame.f_code.co_name,
                "lineno": tb.tb_lineno,
            }
        )
        tb = tb.tb_next

    exception_info = str(
        {"type": type(exception).__name__, "message": str(exception), "trace": trace}
    )

    await context.bot.send_message(
        chat_id=DEV_USER_ID,
        text=f"""Update:
{update}

Caused error:
{exception_info}

Happy debugging on this one!
""",
    )
