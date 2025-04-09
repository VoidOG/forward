from telegram import Update
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext
import logging

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Your bot token
BOT_TOKEN = '7533210168:AAFyBBOO__qmXQ_N-48xscei1eIDllNKqn8'

# Your group and channel usernames (with @), or links
SOURCE_GROUP_USERNAME = '@incognals'     # or use t.me/yourgroup
DEST_CHANNEL_USERNAME = '@incognali'   # or use t.me/yourchannel

def forward_message(update: Update, context: CallbackContext):
    if update.effective_chat.username == SOURCE_GROUP_USERNAME.strip('@'):
        try:
            update.message.forward(chat_id=DEST_CHANNEL_USERNAME)
        except Exception as e:
            print(f"Error forwarding message: {e}")

def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(MessageHandler(Filters.all & Filters.chat(username=SOURCE_GROUP_USERNAME), forward_message))

    updater.start_polling()
    print("Bot is running and listening for messages...")
    updater.idle()

if __name__ == '__main__':
    main()
