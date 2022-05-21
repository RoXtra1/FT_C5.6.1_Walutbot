import telebot
from config import TKN, keys, headers, payload
from extensions import APIException, AskAPI
bot = telebot.TeleBot(TKN) # создаем объект бот

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
    text = 'Вводите названия корректно!\nДоступные валюты:'
    for key in keys.keys():
        text = '\n'.join((text,key))
    bot.reply_to(message, text)

# фильтр содержимого в сообщении, на которое сработает функция ниже (по умолчанию реагирует на текст)
@bot.message_handler()
def convert(message):
    try:
        vals = message.text.split()

        if len(vals) != 3:
            raise APIException('Убедись в правильности введенных параметров')

        base, quote, amount = vals
        result = AskAPI.get_price(base, quote, amount)
    except APIException as e:
        bot.reply_to(message, f'Пользователь ошибся:\n{e}')
    except Exception as e:
        bot.reply_to(message,f'Не могу обработать команду: {e}')
    else:
        text = f'{amount} {keys[base]} = {result:.2f} {keys[quote]}'
        bot.send_message(message.chat.id, text)

bot.polling(none_stop=True) # запуск бота. нон стоп значит что бот должен стараться работать при ошибках