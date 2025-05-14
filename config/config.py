import os
from enum import Enum

from dotenv import load_dotenv

load_dotenv()


class Mode(str, Enum):
    polling = 1
    webhook = 2


MODE = Mode.polling

if MODE == Mode.webhook:
    SECRET_TOKEN = os.getenv("SECRET_TOKEN")  # used in set_webhook
    assert SECRET_TOKEN is not None, "'SECRET_TOKEN' is missing"

    WEBHOOK_URL = os.getenv("WEBHOOK_URL")  # used in set_webhook
    assert WEBHOOK_URL is not None, "'SECRET_TOKEN' is missing"


BOT_TOKEN = os.environ["BOT_TOKEN"]


# developer's user id, used in report_error
DEV_USER_ID = int(os.getenv("DEV_CHAT_ID", -1))
assert DEV_USER_ID != -1, "'DEV_USER_ID' is missing"
