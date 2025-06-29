from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
from config import TELEGRAM_BOT_TOKEN
import logging

logging.basicConfig(level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Alarm AI Bot is running successfully!")

if __name__ == "__main__":
    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()
