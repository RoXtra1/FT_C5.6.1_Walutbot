import requests
import telebot
import json

TKN = "5388159569:AAF5bJz9T5kB48Ayc6FaHrgmbMTKMrEbM2E" # пароль от бота
bot = telebot.TeleBot(TKN) # создаем объект бот

payload = {}
headers= {"apikey": "x55pb7FGx7mik2l9c0NlNVVOa4tP6egV"}

keys = {'евро':'EUR',
        'доллар':'USD',
        'рубль':'RUB'}

# сообщения-команды '/start' или '/help'
@bot.message_handler(commands=['start', 'help'])
def start_help(message):
    text = 'Чтобы начать работу введи через пробел:\n' \
           '<валюту, цену которой хочешь узнать>\n' \
           '<валюту, в цене которой надо узнать первую>\n' \
           '<количество первой валюты>\n\n' \
           'Список доступных валют: /values'
    bot.reply_to(message, text)

# сообщения-команды '/values'
@bot.message_handler(commands=['values'])
def values(message):
    text = 'Доступные валюты:'
    for key in keys.keys():
        text = '\n'.join((text,key))
    bot.reply_to(message, text)

# фильтр содержимого в сообщении, на которое сработает функция ниже (по умолчанию реагирует на текст)
@bot.message_handler()
def convert(message):
    from_w, to_w, amount = message.text.split()
    r = requests.request("GET",
                        url = f"https://api.apilayer.com/exchangerates_data/convert?to={keys[to_w]}&from={keys[from_w]}&amount={amount}",
                        headers=headers,
                        data = payload)
    text = json.loads(r.content)['result']
    bot.send_message(message.chat.id, f'{amount} {keys[from_w]} = {float(text):.2f} {keys[to_w]}')

# реагирует на фото
@bot.message_handler(content_types=['photo'])
def handler_photo(message):
    pass
    #bot.send_photo(chat_id=message.chat.id, photo=['photo'])
    #bot.reply_to(message, "Nice meme XDD")
    #bot.send_message(message.chat.id, "конец функционала")

# Обрабатывается все документы и аудиозаписи
@bot.message_handler(content_types=['document', 'audio'])
def handle_docs_audio(message):
    pass

bot.polling(none_stop=True) # запуск бота. нон стоп значит что бот должен стараться работать при ошибках