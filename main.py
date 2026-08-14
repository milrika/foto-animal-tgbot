import telebot
from dotenv import load_dotenv
import os
from services import get_cat_img

load_dotenv()
API_TOKEN = os.environ.get('API_TOKEN')

bot = telebot.TeleBot(API_TOKEN)

def get_keyboard():
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard = True)
    btn_cat = telebot.types.KeyboardButton('котеки')
    markup.add(btn_cat)

    return markup
    
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, 'prive', reply_markup=get_keyboard())

bot.infinity_polling(skip_pending=True)