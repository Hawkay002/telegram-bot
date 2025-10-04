from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)

# === BOT SETTINGS ===
TOKEN = "8252936732:AAGYulWg2cnqnZ2iyd4ypbpskO1v9qHabwY"
IMAGE_PATH = "Wishing Birthday.png"  # make sure this file is in the same folder as main.py
TRIGGER_MESSAGE = "10/10/2002"    # message that triggers the image

# === /start command ===
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Hi! Send the secret word to get your card!!! ❤️❤️❤️"
    )

# === handle normal text messages ===
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip().lower()

    if text == TRIGGER_MESSAGE.lower():
        await context.bot.send_photo(
            chat_id=update.effective_chat.id,
            photo=open(IMAGE_PATH, "rb")
        )
    else:
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="I only reply to the specific keyword."
        )

# === main entry ===
if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()

    # handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Bot is running...")
    app.run_polling()
