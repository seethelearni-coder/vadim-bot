import logging
import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

logging.basicConfig(level=logging.INFO)
TOKEN = os.environ.get("BOT_TOKEN")
FILE_PATH = "Автопрогрев через РСЯ. Вадим Альшин.xmind"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    await update.message.reply_text(
        f"Привет, {user.first_name} 👋\n\n"
        "Держи майнд-карту — 7-шаговая система стабильных заявок.\n\n"
        "Приятного изучения и если захочешь разобрать как это работает именно в твоей нише — "
        "пиши: @vadimarket"
    )
    with open(FILE_PATH, "rb") as f:
        await update.message.reply_document(
            document=f,
            filename="Система заявок Вадим Альшин.xmind",
            caption="7-шаговая система стабильных заявок для экспертов 🔥"
        )

app
