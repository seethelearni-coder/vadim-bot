import asyncio
import logging
import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

logging.basicConfig(level=logging.INFO)
TOKEN = os.environ.get("BOT_TOKEN")
FILE_PATH = "Автопрогрев_через_РСЯ_Вадим_Альшин.xmind"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    await update.message.reply_text(
        f"Привет, {user.first_name} 👋\n\n"
        "Держи майнд-карту — 7-шаговая система стабильных заявок для экспертов.\n\n"
        "Приятного изучения, если будут вопросы, смело пиши мне @vadimarket"
    )
    with open(FILE_PATH, "rb") as f:
        await update.message.reply_document(
            document=f,
            filename="Система_заявок_Вадим_Альшин.xmind",
            caption="7-шаговая система стабильных заявок для экспертов 🔥"
        )

async def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("Бот запущен...")
    await app.run_polling()

if __name__ == "__main__":
    asyncio.run(main())
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("Бот запущен...")
    app.run_polling()
