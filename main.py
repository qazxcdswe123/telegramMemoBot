import os
import logging

import requests
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Init params 
BOT_TOKEN = os.environ.get('BOT_TOKEN')
CHAT_ID = os.environ.get('CHAT_ID')
MEMO_API = os.environ.get('MEMO_API')

# API_BASE_URL = "https://memos.example.com/api/"
API_BASE_URL = MEMO_API.split('memo?')[0]
# BASE_URL = "https://memos.example.com/"
BASE_URL = API_BASE_URL.split('api/')[0]
OPENID = MEMO_API.split('=')[1]

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

logger = logging.getLogger(__name__)


# Define a few command handlers
def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi! The bot is up and running!')


def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('See https://github.com/qazxcdswe123/telegramMemoBot')


# Handle messages
def memo(update, context):
    """Add the user message to float."""
    chat_id = update.message.chat.id
    if chat_id != int(CHAT_ID):
        update.message.reply_text('You are not the owner of this bot. Only the owner can use this bot.')
    else:
        tags = []
        for i in update.message.text.split():
            if i.startswith('#'):
                # find until the next space or the end of the string
                tags.append(i[1:].split(' ')[0])
        if tags:
            for tag in tags:
                tag_data = {"name": tag}
                requests.post(API_BASE_URL + 'tag?openId=' + OPENID, json=tag_data)
        data = {"content": update.message.text}
        r = requests.post(API_BASE_URL + "memo?openId=" + OPENID, json=data)
        update.message.reply_text('{} {}'.format(r.status_code, r.reason))


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(BOT_TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    # on noncommand i.e message - echo the message on Telegram
    # dp.add_handler(MessageHandler(Filters.text, echo))
    dp.add_handler(MessageHandler(Filters.text, memo))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
