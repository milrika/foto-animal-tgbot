import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from dotenv import load_dotenv
import os
from services import get_cat_img, get_duck_img, get_dog_img

load_dotenv()
API_TOKEN = os.environ.get('API_TOKEN')

bot = telebot.TeleBot(API_TOKEN)
    
@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    btn_cat = KeyboardButton('котеки')
    btn_duck = KeyboardButton('утке')
    btn_dog = KeyboardButton('собако')
    markup.add(btn_cat, btn_duck, btn_dog)

    bot.send_message(message.chat.id, 'prive', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def send_img(message):
    if message.text == 'котеки':
        bot.send_photo(message.chat.id, get_cat_img(), caption='привет, я котек!')

    elif message.text == 'утке':
        bot.send_photo(message.chat.id, get_duck_img(), 'привет, я утка!')

    elif message.text == 'собако':
        bot.send_photo(message.chat.id, get_dog_api(), 'привет, я собако!')


bot.infinity_polling(skip_pending=True)