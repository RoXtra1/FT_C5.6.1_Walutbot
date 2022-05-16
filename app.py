import telebot
import json

TKN = "5388159569:AAF5bJz9T5kB48Ayc6FaHrgmbMTKMrEbM2E" # пароль от бота
bot = telebot.TeleBot(TKN) # создаем объект бот

# сообщения-команды '/start' или '/help'.
@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
    pass
    #bot.send_message(message.chat.id, "а че придумать то кстати ну пусть будет хуй попробуй фотку скинуть")

# фильтр содержимого в сообщении, на которое сработает функция ниже (по умолчанию реагирует на текст)
@bot.message_handler()
def handler_text(message):
    pass
    #print(f'сообщение: {message.text}')
    #bot.send_message(message.chat.id, f"моя любимая {message.chat.first_name}na")
    #bot.reply_to(message, str(input('ответ: \t')))

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