![Ruff Formatter](https://img.shields.io/badge/style-ruff-000000.svg?logo=python&logoColor=white)


# Python Telegram Bot Starter Kit with Starlette

I often use this structure when building web-powered Telegram bots. After reusing it so many times, I decided to organize it nicely and share it here. Hope it helps you get started faster!

---
## Features

- **Error Reporting**: Reports Telegram bot exceptions to the developer as a direct message.
- **Localization**: Support for multiple languages with a simple setup.
- **Persistence**: Preconfigured to use a pickled persistence object.
- **Webhook and Polling Modes**: Easily switch between polling and webhook modes by editing the `MODE` constant in `config/config.py`.

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
└── run.py                 # Main entry point
```

---

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/ptb-starlette-starter.git
   cd ptb-starlette-starter
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up the `.env` file by copying `.env.example` and filling in the necessary variables:
   ```bash
   cp .env.example .env
   ```

4. Run the webserver:
   ```bash
   uvicorn run:app
   ```

---

## Switching Between Polling and Webhook Modes

This starter allows you to easily switch between polling and webhook modes. In the `config/config.py` file, modify the `MODE` constant to set your preferred mode:

- `MODE = Mode.polling`: Uses long polling to fetch updates.
- `MODE = Mode.webhook`: Configures the bot to use webhooks.

---

## Use Cases for Running PTB with Starlette

Here’s why combining `python-telegram-bot` with Starlette is awesome:

1. **Telegram Miniapps**: Want to build a [Telegram miniapp](https://core.telegram.org/bots/webapps)? This setup lets you handle both your bot and miniapp with a single backend, making communication between them super smooth.
2. **Telegram Games**: If your bot uses [Telegram's game platform](https://core.telegram.org/bots/games), running your bot and web server together simplifies the whole process of keeping them in sync.
3. **Web Extensions**: Thinking about extending your bot’s features to a website? Maybe a dashboard to track stats or control the bot? This is the perfect way to do it.
4. **Endless Possibilities**: From integrating external APIs to hosting RESTful or GraphQL endpoints, running PTB with Starlette opens the door to countless creative solutions.

---

## Contributing

Contributions are welcome! Feel free to fork the repository, create a branch, and submit a pull request.

---

## Acknowledgements

- [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)
- [Starlette](https://github.com/encode/starlette)
