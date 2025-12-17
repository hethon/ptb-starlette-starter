![Ruff Formatter](https://img.shields.io/badge/style-ruff-000000.svg?logo=python&logoColor=white)


# Python Telegram Bot Starter Kit with Starlette

I often use this structure when building web-powered Telegram bots. After reusing it so many times, I decided to organize it nicely and share it here. Hope it helps you get started faster!

---
## Features

- **Error Reporting**: Sends runtime exceptions as direct messages to a specified chat, group, or channel using `ERROR_LOG_CHAT_ID`.
- **Localization**: Support for multiple languages with a simple setup.
- **Persistence**: Preconfigured to use Async Sqlalchemy 2.0 with SQLite.
- **Webhook and Polling Modes**: Control the update mode via environment variables:
  - Set both `SECRET_TOKEN` and `WEBHOOK_URL` to enable webhook mode
  - If either is unset, the bot falls back to polling
- **Telegram Test Server Support**: Switch between Telegram production and test servers via environment variables:
  - Set `USE_TEST_SERVER=yes` and `TEST_SERVER_BOT_TOKEN` to use the test server
  - If `USE_TEST_SERVER` is not set, the bot uses the production server
  - **Note:** `TEST_SERVER_BOT_TOKEN` is required if `USE_TEST_SERVER=yes`

---

## Folder Structure

```
ptb-starlette-starter
├── config/                # Configuration and localization
│   ├── config.py          # Main configuration file
│   └── locale/            # Locale files
├── persistence/           # persistence files
├── ptb/                   # Telegram bot logic
│   ├── handlers.py        # Command and message handlers
│   ├── custom_context.py  # Custom context implementation
│   ├── custom_updates.py  # Custom update definitions
│   ├── error_handler.py   # Error handling logic
│   ├── helpers.py         # Helper functions
│   ├── post_init.py       # Post-initialization logic
│   └── tg_app.py          # Main bot application
├── stl/                   # Starlette application logic
│   ├── routes.py          # Starlette routes
│   └── starlette_app.py   # Starlette app configuration
├── scripts/               # Utility scripts
│   └── set_webhook.py     # Script to set webhooks
├── .env.example           # Example environment file
├── requirements.txt       # Python dependencies
└── main.py                # Main entry point
```

---

### Installation

This project uses UV for dependency managment.

1. create your project directory and cd into it:
   ```bash
   mkdir my-project
   cd my-project
   ```

2. Clone this repository:
   ```bash
   git clone https://github.com/hethon/ptb-starlette-starter.git .
   ```

3. Set up the `.env` file by copying `.env.example` and filling in the necessary variables:
   ```bash
   cp .env.example .env
   ```

4. Run the Alembic migration script
   ```bash
   uv run -- alembic upgrade head
   ```

   - The first time you run a uv run command, uv will automatically create a virtual environment and install dependencies.
   - `alembic upgrade head` will set up the demo database schema (create the demo table) so the bot can start working right away.

5. Run the webserver with uvicorn or any ASGI server of your choice:
   ```bash
   uv run -- uvicorn main:app
   ```

---

## Switching Between Polling and Webhook Modes

The project runs in webhook mode if WEBHOOK_URL is set and not commented out in .env; otherwise, it defaults to polling mode.

## Use Cases for Running PTB with Starlette

- If you are building a [Telegram miniapp](https://core.telegram.org/bots/webapps), this setup lets you handle both your bot and miniapp with a single backend, making communication between them fast and easy.

- If your bot uses [Telegram's game platform](https://core.telegram.org/bots/games), running your bot and web server together simplifies the whole process of keeping them in sync.

- If you think about monitoring/controlling your bot's state via a website, this setup makes it easy as you can simply create endpoints to do that.

---

## Contributing

Contributions are welcome! Feel free to fork the repository, create a branch, and submit a pull request.

---

## Acknowledgements

- [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)
- [Starlette](https://github.com/encode/starlette)
