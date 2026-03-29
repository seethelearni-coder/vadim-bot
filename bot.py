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
        "Держи майнд-карту — система автопрогрева с помощью РСЯ.\n\n"
        "Приятного изучения и если захочешь разобрать как это работает именно в твоей нише — "
        "пиши: @vadimarket"
    )
    with open(FILE_PATH, "rb") as f:
        await update.message.reply_document(
            document=f,
            filename="Система заявок Вадим Альшин.xmind",
            caption="Чтобы открыть файл правильно:\nСкачай Xmind на телефон или компьютер, открой файл с помощью данной программы.\n\nЕсли тебе лень даже на данном этапе, тебе не нужны клиенты и деньги)"
        )

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
print("Бот запущен...")
app.run_polling()
