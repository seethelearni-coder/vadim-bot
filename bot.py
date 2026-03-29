import logging
import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

logging.basicConfig(level=logging.INFO)

TOKEN = "8582326175:AAHNHdJIHxtrC6Khtvi5Sen-OjUmKfJoDvM"
FILE_PATH = "mindmap.xmind"  # файл майнд-карты рядом с bot.py

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    await update.message.reply_text(
        f"Привет, {user.first_name} 👋\n\n"
        "Держи майнд-карту — 7-шаговая система стабильных заявок для экспертов.\n\n"
        "Изучи, внедри, и если захочешь разобрать как это работает именно в твоей нише — "
        "пиши: @vadimarket"
    )
    with open(FILE_PATH, "rb") as f:
        await update.message.reply_document(
            document=f,
            filename="Система_заявок_Вадим_Альшин.xmind",
            caption="7-шаговая система стабильных заявок для экспертов 🔥"
        )

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("Бот запущен...")
    app.run_polling()
