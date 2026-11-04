import os
import logging
import telebot
from datetime import datetime

TOKEN = os.getenv("TELEGRAM_TOKEN")

if not TOKEN:
    raise RuntimeError("Token Telegram non configurato")

bot = telebot.TeleBot(TOKEN)

logging.basicConfig(level=logging.INFO)

@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(
        message,
        "⚽ TIPSTER PRO\n\n"
        "Benvenuto nel tuo centro di analisi calcistica.\n\n"
        "Comandi disponibili:\n"
        "/analisi - Analisi calcistiche\n"
        "/oggi - Programma giornaliero\n"
        "/bankroll - Gestione bankroll\n"
        "/info - Informazioni sul bot"
    )

@bot.message_handler(commands=["info"])
def info(message):
    bot.reply_to(
        message,
        "TIPSTER PRO\n"
        "Sistema di analisi e statistiche calcistiche.\n"
        "Le analisi non garantiscono vincite."
    )

@bot.message_handler(commands=["analisi"])
def analisi(message):
    bot.reply_to(
        message,
        "🔎 Motore di analisi in configurazione.\n"
        "Le previsioni saranno pubblicate solo quando "
        "saranno disponibili dati verificabili."
    )

@bot.message_handler(commands=["oggi"])
def oggi(message):
    data = datetime.now().strftime("%d/%m/%Y")
    bot.reply_to(
        message,
        f"📅 Programma del {data}\n\n"
        "Calendario e statistiche in fase di collegamento."
    )

@bot.message_handler(commands=["bankroll"])
def bankroll(message):
    bot.reply_to(
        message,
        "💰 Gestione bankroll\n"
        "Configurazione iniziale non ancora completata."
    )

logging.info("TIPSTER PRO avviato")
bot.infinity_polling()
