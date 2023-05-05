# Telegram fast search

This is a script that searches for messages in Telegram chats and forwards them to a selected chat.

## Installation

Clone this repository to your local machine with git, create a virtual environment and install the requirements.

```bash
git clone https://github.com/vasyapeteckin/tg-fast-search.git
cd tg-fast-search
```

## Basic Usage

In the `.env` file, configure `API_ID=` and `API_HASH=` to obtain your Telegram API keys [here](https://my.telegram.org/auth?to=apps).

### Configuring the Settings File:

`timedelta_hours` = maximum time delta

`chat_id_to_forward` = your chat_id (you can use [this bot](https://t.me/getmyid_bot) to get your ID)

`key_words` = a list of strings with keywords (e.g. ["zetachain", "layerzero", ...])

```bash
python main.py
```