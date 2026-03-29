import logging
import os
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

logging.basicConfig(level=logging.INFO)
TOKEN = os.environ.get("BOT_TOKEN")
FILE_PATH = "Автопрогрев через РСЯ. Вадим Альшин.xmind"

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot is running")
    def log_message(self, format, *args):
        pass

def run_server():
    server = HTTPServer(("0.0.0.0", 8080), Handler)
    server.serve_forever()

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

threading.Thread(target=run_server, daemon=True).start()
app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
print("Бот запущен...")
app.run_polling()
