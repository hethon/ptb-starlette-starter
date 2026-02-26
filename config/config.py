import os
from enum import Enum

from dotenv import load_dotenv

load_dotenv()


class UpdateMode(Enum):
    POLLING = 1
    WEBHOOK = 2

    @classmethod
    def from_env(cls) -> "UpdateMode":
        if "SECRET_TOKEN" in os.environ and "WEBHOOK_URL" in os.environ:
            return cls.WEBHOOK
        return cls.POLLING


update_mode = UpdateMode.from_env()
SECRET_TOKEN = os.environ.get("SECRET_TOKEN")
WEBHOOK_URL = os.environ.get("WEBHOOK_URL")

BOT_TOKEN = os.environ["BOT_TOKEN"]
USE_TEST_SERVER = os.environ.get("USE_TEST_SERVER") == "yes"
TEST_SERVER_BOT_TOKEN = os.environ.get("TEST_SERVER_BOT_TOKEN", "")
if USE_TEST_SERVER and not TEST_SERVER_BOT_TOKEN:
    raise Exception(  # noqa: TRY002
        "USE_TEST_SERVER is set to yes, but TEST_SERVER_BOT_TOKEN is missing."
        "Please set TEST_SERVER_BOT_TOKEN or disable USE_TEST_SERVER."
    )


# developer's user id, used in report_error
ERROR_LOG_CHAT_ID = int(os.environ["ERROR_LOG_CHAT_ID"])

DATABASE_URL = os.environ["DATABASE_URL"]
