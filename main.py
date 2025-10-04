import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

TOKEN = os.environ.get("TOKEN")
IMAGE_FILE = "Birthday Wish.png"  # your picture file

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Hi! Send the secret word to get your card!!!❤️ ❤️ ❤️")

def send_image(update: Update):
    update.message.reply_photo(open(IMAGE_FILE, 'rb'))

def handle_message(update: Update, context: CallbackContext):
    text = update.message.text.lower()
    if "10/10/2002" in text:
        send_image(update)
    else:
        update.message.reply_text("Wrong word! Try again.")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & (~Filters.command), handle_message))

    print("Bot is running...")
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
