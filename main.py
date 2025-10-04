from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

TOKEN = "8252936732:AAGYulWg2cnqnZ2iyd4ypbpskO1v9qHabwY"
IMAGE_PATH = "Birthday Wish.png"  # make sure this file is in the same folder as main.py
TRIGGER_MESSAGE = "10/10/2002"  # the specific message that triggers the image

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Check if the received message matches the trigger
    if update.message.text and update.message.text.lower() == TRIGGER_MESSAGE.lower():
        await update.message.reply_photo(photo=open(IMAGE_PATH, "rb"))
    else:
        await update.message.reply_text("I only respond to the specific trigger message.")

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()

    # MessageHandler listens for text messages
    handler = MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message)
    app.add_handler(handler)

    # Start the bot
    app.run_polling()
