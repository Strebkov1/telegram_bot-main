import telebot
from telebot import types
import random
import os

bot = telebot.TeleBot("6733869167:AAEwXBNpLoxycOfCiUpPoCe7wKToTjAUPAI")

meal = ['Паста', 'Пицца', 'Пельмени', 'Суп', 'Фанта']

@bot.message_handler(commands=["start"])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton("Рандомное число"))
    markup.add(types.KeyboardButton("Рандомное блюдо"))
    markup.add(types.KeyboardButton("Рандомный стикер"))
    bot.send_message(message.chat.id, "Выберите действие", reply_markup=markup)

@bot.message_handler(commands=["hello"])
def hello(message):
    bot.send_message(message.chat.id, "Привет")

@bot.message_handler(content_types=["text"])
def randomize(message):
    if message.text == 'Рандомное число':
        num = random.randint(1, 100)
        bot.send_message(message.chat.id, str(num))

    if message.text == 'Рандомное блюдо':
        drinks = random.choice(meal)
        bot.send_message(message.chat.id, drinks)

    if message.text == 'Рандомный стикер':
        sticker = os.path.join('./721424997', random.choice(os.listdir('./721424997')))
        bot.send_sticker(message.chat.id, open(sticker, 'rb'))

bot.polling(none_stop=True)
