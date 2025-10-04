from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = "8252936732:AAGYulWg2cnqnZ2iyd4ypbpskO1v9qHabwY"

# Command /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hi! Send the secret word to get your card!!!")

# Handle messages
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.text.lower() == "10/10/2002":
        await update.message.reply_photo(open("Birthday Wish.png", "rb"))

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))

# Run the bot
app.run_polling()
