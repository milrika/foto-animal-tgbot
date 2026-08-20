import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from dotenv import load_dotenv
import os
from services import get_cat_img, get_duck_img, get_dog_img, get_taxik_img

load_dotenv()
API_TOKEN = os.environ.get('API_TOKEN')

bot = telebot.TeleBot(API_TOKEN)
    
@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    btn_cat = KeyboardButton('котеки')
    btn_duck = KeyboardButton('утке')
    btn_dog = KeyboardButton('собако')
    btn_taxik = KeyboardButton('🌭🌭!!!')
    markup.add(btn_cat, btn_duck, btn_dog, btn_taxik)

    bot.send_message(message.chat.id, 'prive', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def send_img(message):
    if message.text == 'котеки':
        url = get_cat_img()

        if url:
            try:
                bot.send_photo(message.chat.id, url, caption='привет, я котек!')
            except Exception as e: print(f'ошибка {e}')
        else:
            bot.send_message(message.chat.id, 'Неудалось достать фото кота')

    elif message.text == 'утке':
        url = get_duck_img()

        if url:
            try:
                bot.send_photo(
                    message.chat.id, url, 'привет, я утка!')
            except Exception as e:
                print(f'ошибка {e}')
        else:
            bot.send_message(message.chat.id, 'Неудалось достать фото утки')
                 

    elif message.text == 'собако':
        url = get_dog_img()

        if url:
            try:
                bot.send_photo(message.chat.id, url, 'привет, я собако!')
            except Exception as e:
                print(f'ошибка {e}')
        else:
            bot.send_message(message.chat.id, 'Неудалось достать фото собаки')

    elif message.text == '🌭🌭!!!':
        url = get_taxik_img()

        if url:
            try:
                bot.send_photo(message.chat.id, url, 'привет, я 🌭🌭!!!')
            except Exception as e:
                print(f'ошибка {e}')
        else:
            bot.send_message(message.chat.id, 'Неудалось достать фото 🌭🌭')

bot.infinity_polling(skip_pending=True)