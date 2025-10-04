import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = os.environ.get("TOKEN")
IMAGE_FILE = "Birthday Wish.png"  # your uploaded picture file

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.args and "sendpic" in context.args[0].lower():
        await send_image(update)
    else:
        await update.message.reply_text("Hi! Send the secret word to get your card!!!❤️ ❤️ ❤️")

# Function to send image
async def send_image(update: Update):
    try:
        await update.message.reply_photo(open(IMAGE_FILE, 'rb'))
    except Exception as e:
        await update.message.reply_text(f"Error sending image: {e}")

# Handle text messages
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()
    if "10/10/2002" in text:
        await send_image(update)
    else:
        await update.message.reply_text("Wrong word! Try again.")

# Main function
def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
