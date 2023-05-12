import json
import os
import yaml

from datetime import datetime, timedelta

from dotenv import load_dotenv
from pyrogram import Client


async def fast_search(key_words: list[str] = None):
    start_time = datetime.now()

    with open('settings.yaml', 'r') as f:
        settings = yaml.safe_load(f)

    chat_id_to_forward = settings.get('chat_id_to_forward')

    async with app:
        for key_word in settings["key_words"]:
            async for message in app.search_global(query=key_word):
                time_difference = start_time - message.date

                if message.chat.username:
                    url = f"https://t.me/{message.chat.username}/{message.id}"
                else:
                    url = f"https://t.me/c/{str(message.chat.id)[4:]}/{message.id}"

                text = f"**[{message.chat.title}]({url})**\n\n{message.text}"

                if message.chat.id != int(chat_id_to_forward):
                    if message.from_user:
                        await app.send_message(chat_id=chat_id_to_forward, text=text)
                    else:
                        await message.forward(chat_id=chat_id_to_forward)

                    if time_difference > timedelta(hours=settings['timedelta_hours']):
                        break

    print(datetime.now() - start_time)


if __name__ == '__main__':
    load_dotenv()
    api_id = os.getenv('API_ID')
    api_hash = os.getenv('API_HASH')

    app = Client("my_account", api_id=api_id, api_hash=api_hash)

    app.run(fast_search())
