import os
import logging
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import (
    CommandHandler,
    Updater,
    CallbackContext,
    MessageHandler,
    Filters,
)

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

load_dotenv()
my_token = os.getenv("TOKEN")
updater = Updater(token=my_token, use_context=True)
dispatcher = updater.dispatcher


def start(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm the Red Squadron Telegram bot, type this "
                                                                    "command to get your Chat ID for receiving "
                                                                    "telegram notifications. @get_id_bot /my_id")


def notify(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Type this command to get your Chat"
                                                                    " ID for receiving telegram notifications from "
                                                                    "Overseerr. @get_id_bot /my_id")


if __name__ == '__main__':
    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    notify_handler = CommandHandler('notify', notify)
    dispatcher.add_handler(notify_handler)

    updater.start_polling()
