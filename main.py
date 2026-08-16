import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from dotenv import load_dotenv
import os
from services import get_cat_img

load_dotenv()
API_TOKEN = os.environ.get('API_TOKEN')

bot = telebot.TeleBot(API_TOKEN)
    
@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    btn_cat = KeyboardButton('котеки')
    markup.add(btn_cat)

    bot.send_message(message.chat.id, 'prive', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def send_img(message):
    print('робит')
    if message.text == 'котеки':
        bot.send_photo(message.chat.id, get_cat_img(), caption='привет я котек!')


bot.infinity_polling(skip_pending=True)