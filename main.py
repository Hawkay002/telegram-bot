from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

# Your bot token
TOKEN = "8252936732:AAGYulWg2cnqnZ2iyd4ypbpskO1v9qHabwY"

# File to send
IMAGE_PATH = "Birthday Wish.png"  # make sure this file is in the same folder as main.py

# Trigger message
TRIGGER_MESSAGE = "10/10/2002"  # the secret word or phrase

# --- Command handler ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hi! Send the secret word you just copied to get your card!❤️ ❤️ ❤️")

# --- Message handler ---
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.text and update.message.text.lower() == TRIGGER_MESSAGE.lower():
        await update.message.reply_photo(photo=open(IMAGE_PATH, "rb"))
    else:
        await update.message.reply_text("I only reply to the specific keyword.")

# --- Main program ---
if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()

    # Register handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))

    # Start polling
    app.run_polling()
