import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackContext, filters

TOKEN = os.environ.get("TOKEN")
IMAGE_FILE = "Birthday Wish.png"  # make sure this file exists

def start(update: Update, context: CallbackContext):
    if context.args and "sendpic" in context.args[0].lower():
        send_image(update)
    else:
        update.message.reply_text("Hi! Send the secret word to get your card!!!❤️ ❤️ ❤️")

def send_image(update: Update):
    try:
        update.message.reply_photo(open(IMAGE_FILE, 'rb'))
    except Exception as e:
        update.message.reply_text(f"Error sending image: {e}")

def handle_message(update: Update, context: CallbackContext):
    text = update.message.text.lower()
    if "10/10/2002" in text:
        send_image(update)
    else:
        update.message.reply_text("Wrong word! Try again.")

def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start, pass_args=True))
    dp.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
