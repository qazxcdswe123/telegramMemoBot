import asyncio
import logging
import os
from threading import Lock

from api import Memo, Resource

# from telebot import apihelper
from telebot.async_telebot import AsyncTeleBot

CHAT_ID = os.getenv("CHAT_ID")
MEMO_API = os.getenv("MEMO_API")
BOT_TOKEN = os.getenv("BOT_TOKEN")

# DOMAIN = http://localhost:5230/
DOMAIN = MEMO_API.split("api/")[0]
OPENID = MEMO_API.split("=")[1]
CHAT_IDs = CHAT_ID.split(",")
bot = AsyncTeleBot(BOT_TOKEN)
lock = Lock()

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

logger = logging.getLogger(__name__)


def auth(func):
    async def wrapper(message):
        if str(message.chat.id) in CHAT_IDs:
            await func(message)
        else:
            logging.warning(f"Unauthorized access: {message.chat.id}")
            await bot.reply_to(message, "Unauthorized access")

    return wrapper


def get_file_id(message) -> str:
    try:
        file_id = getattr(message, message.content_type)[-1].file_id
    except Exception:
        file_id = getattr(message, message.content_type).file_id
    return file_id


@bot.message_handler(commands=["start", "help"])
async def send_help(message):
    logging.info(f"Help message sent to {message.chat.id}")
    await bot.reply_to(message, "https://github.com/qazxcdswe123/telegramMemoBot")


@bot.message_handler(content_types=["text"])
@auth
async def send_text_memo(message):
    try:
        memo = Memo(DOMAIN, OPENID)
        memo_id = await memo.send_memo(content=message.text)
        logging.info(f"Memo sent: {DOMAIN}m/{memo_id}")
        await bot.reply_to(message, f"{DOMAIN}m/{memo_id}")
    except Exception as e:
        logging.error(f"Error: {e} in send_text_memo")
        await bot.reply_to(message, f"Error: {e}")


media_group = {}


@bot.message_handler(content_types=["photo"])
@auth
async def send_photo_memo(message):
    if message.media_group_id:
        logging.info(f"Media group ID: {message.media_group_id}")
        with lock:
            # Shouldn't download here since download is slow
            fid = get_file_id(message)
            prev_val = media_group.get(message.media_group_id)
            if prev_val:
                prev_val["fid_list"].append(fid)
                if message.caption:
                    prev_val["caption"].append(message.caption)
            else:
                init_val = {
                    "message": message,
                    "caption": message.caption or "",
                    "fid_list": [fid],
                }
                media_group[message.media_group_id] = init_val
    else:
        # only one photo
        try:
            file_info = await bot.get_file(get_file_id(message))
            file = await bot.download_file(file_info.file_path)

            res = Resource(DOMAIN, OPENID)
            res_id = await res.create_res(file)
            memo = Memo(DOMAIN, OPENID)
            memo_id = await memo.send_memo(
                content=message.caption, res_id_list=[res_id]
            )
            await bot.reply_to(message, f"{DOMAIN}m/{memo_id}")
        except Exception as e:
            logging.error(f"Error: {e} in send_photo_memo")
            await bot.reply_to(message, f"Error: {e}")


# Periodically check if there is any media group ready to send
async def multi_photo_checker():
    while True:
        logging.debug(f"Multi photo checker started")
        for unique, data in list(media_group.items()):
            logging.info(f"Set {unique} is ready to send")
            file_list = []
            res_id_list = []
            for fid in data["fid_list"]:
                file_info = await bot.get_file(fid)
                file = await bot.download_file(file_info.file_path)
                file_list.append(file)
            res = Resource(DOMAIN, OPENID)
            for f in file_list:
                res_id = await res.create_res(f)
                res_id_list.append(res_id)
            media_group.pop(unique)
            memo = Memo(DOMAIN, OPENID)
            memo_id = await memo.send_memo(
                content=data["caption"], res_id_list=res_id_list
            )
            await bot.reply_to(data["message"], f"{DOMAIN}m/{memo_id}")
        await asyncio.sleep(5)


async def main():
    await asyncio.gather(bot.polling(), multi_photo_checker())


if __name__ == "__main__":
    asyncio.run(main())
