import telebot
from dotenv import load_dotenv
import os

load_dotenv()
API_TOKEN = os.environ.get('API_TOKEN')

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'привет я попа')

bot.infinity_polling()