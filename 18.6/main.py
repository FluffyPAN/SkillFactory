# подцепляем файлы и библиотеки
import telebot
from config import keys, TOKEN
from extensions import ConversionException, CryptoConvertor

bot = telebot.TeleBot(TOKEN)  # создаём бота


@bot.message_handler(commands=['start', 'help'])  # обработка команд старт и помощь
def help_start(message: telebot.types.Message):
    text = "Чтобы начать работу введите команду боту в следующем формате: \n(имя валюты)"\
           " (В какую перевести) (количесвто переводимой валюты)" \
           "\nготовые команды:\n /values"
    bot.reply_to(message, text)


@bot.message_handler(commands=['values'])  # обработка команды значения
def values(message: telebot.types.Message):
    text = "Доступные валюты:"
    for key in keys.keys():
        text = '\n'.join((text, key))
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text'])  # обработка основной функции
def convert(message: telebot.types.Message):
    try:
        values_for_next = message.text.split(" ")

        if len(values_for_next) != 3:
            raise ConversionException("Неверное количество параметров")

        quote, base, amount = values_for_next
        total_base = CryptoConvertor.get_price(quote, base, amount)
    except ConversionException as e:
        bot.reply_to(message, f"Ошибка пользователя\n{e}")  # ошибка пользователя
    except Exception as e:
        bot.reply_to(message, f"Не удалось обработать команду\n{e}")  # ошибка кода
    else:
        text = f"цена {amount} {quote} в {base} - {total_base}"  # вывод результата
        bot.send_message(message.chat.id, text)


bot.polling()
