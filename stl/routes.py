from http import HTTPStatus

from starlette.requests import Request
from starlette.responses import PlainTextResponse, Response
from telegram import Update

import config.config as config
from ptb.custom_updates import CustomUpdate
from ptb.tg_app import tg_app


async def telegram(request: Request) -> Response:
    """Handle incoming Telegram updates by putting them into the `update_queue`"""
    secret_token = request.headers.get("X-Telegram-Bot-Api-Secret-Token")
    if secret_token != config.SECRET_TOKEN:
        # update is not from telegram
        return Response(status_code=HTTPStatus.UNAUTHORIZED)

    await tg_app.update_queue.put(
        Update.de_json(data=await request.json(), bot=tg_app.bot)
    )
    return Response()


async def custom_updates(request: Request) -> PlainTextResponse:
    """Handle incoming custom updates by putting them into the `update_queue`"""
    user_id = request.query_params.get("user_id")
    payload = request.query_params.get("payload")
    if not user_id:
        return PlainTextResponse(
            "user_id is missing", status_code=HTTPStatus.BAD_REQUEST
        )

    if not payload:
        return PlainTextResponse(
            "payload is missing", status_code=HTTPStatus.BAD_REQUEST
        )

    try:
        user_id = int(user_id)
    except ValueError:
        return PlainTextResponse(
            "user_id must be an integer", status_code=HTTPStatus.BAD_REQUEST
        )

    await tg_app.update_queue.put(CustomUpdate(user_id=user_id, payload=payload))

    return PlainTextResponse("success.")


async def health(_: Request) -> PlainTextResponse:
    """For the health endpoint, reply with a simple plain text message."""
    return PlainTextResponse(content="The bot is still running fine :)")
