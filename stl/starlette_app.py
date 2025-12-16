from collections.abc import AsyncIterator
from contextlib import asynccontextmanager
from typing import TypedDict

from starlette.applications import Starlette
from starlette.routing import Route

from config import config
from ptb.post_init import post_init
from ptb.tg_app import tg_app
from scripts.set_webhook import set_webhook

from .routes import custom_updates, health, telegram


class State(TypedDict):
    pass


@asynccontextmanager
async def lifespan_polling(app: Starlette) -> AsyncIterator[State]:  # noqa: ARG001
    async with tg_app:
        await post_init(tg_app)
        await tg_app.start()
        await tg_app.updater.start_polling()
        yield {}
        await tg_app.updater.stop()
        await tg_app.stop()


@asynccontextmanager
async def lifespan_webhook(app: Starlette) -> AsyncIterator[State]:  # noqa: ARG001
    await set_webhook()
    async with tg_app:
        await post_init(tg_app)
        await tg_app.start()
        yield {}
        await tg_app.stop()


starlette_app = Starlette(
    routes=[
        Route("/bot", telegram, methods=["POST"]),  # used for webhook mode
        Route("/healthcheck", health, methods=["GET"]),
        Route("/submitpayload", custom_updates, methods=["POST", "GET"]),
    ],
    lifespan=(
        lifespan_webhook if config.Mode.webhook == config.MODE else lifespan_polling
    ),
)
