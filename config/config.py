import os
from enum import Enum

from dotenv import load_dotenv

load_dotenv()


class Mode(str, Enum):
    polling = 1
    webhook = 2


MODE = Mode.webhook
try:
    SECRET_TOKEN = os.environ["SECRET_TOKEN"]
    WEBHOOK_URL = os.environ["WEBHOOK_URL"]
except KeyError:
    MODE = Mode.polling


BOT_TOKEN = os.environ["BOT_TOKEN"]

# developer's user id, used in report_error
DEV_USER_ID = int(os.environ["DEV_CHAT_ID"])

DATABASE_URL = os.environ["DATABASE_URL"]
