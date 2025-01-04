from contextlib import asynccontextmanager
from typing import TypedDict
from collections.abc import AsyncIterator

from starlette.applications import Starlette
from starlette.routing import Route

from .routes import telegram, custom_updates, health
from ptb.tg_app import tg_app
from ptb.post_init import post_init
from scripts.set_webhook import set_webhook
import config.config as config




class State(TypedDict):
    pass


@asynccontextmanager
async def lifespan_polling(app: Starlette) -> AsyncIterator[State]:
    async with tg_app:
        await post_init(tg_app)
        await tg_app.start()
        await tg_app.updater.start_polling()
        yield
        await tg_app.updater.stop()
        await tg_app.stop()


@asynccontextmanager
async def lifespan_webhook(app: Starlette) -> AsyncIterator[State]:
    await set_webhook()
    async with tg_app:
        await post_init(tg_app)
        await tg_app.start()
        yield
        await tg_app.stop()


starlette_app = Starlette(
    routes=[
        Route(f"/bot", telegram, methods=["POST"]),  # used for webhook mode
        Route("/healthcheck", health, methods=["GET"]),
        Route("/submitpayload", custom_updates, methods=["POST", "GET"]),
    ],
    lifespan=(
        lifespan_webhook if config.MODE == config.Mode.webhook else lifespan_polling
    ),
)
