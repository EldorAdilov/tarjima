from translate import translate
import telebot

TOKEN = "6912086859:AAFjrbeF3FY3L6GM4tsPDmV7ty0qx9uDEHU"
tarjimonbot = telebot.TeleBot(token=TOKEN)


@tarjimonbot.message_handler(commands=['start'])
def salom(message):
    xabar = "Assalomu alaykum tarjimon botga hush kelibsiz, bu bot tarjima qiladi."
    xabar += '\nMatningizni yuboring'
    tarjimonbot.reply_to(message, xabar)


@tarjimonbot.message_handler(func=lambda msg: msg.text is not None)
def tarjima(message):
    msg = message.text
    tarjimonbot.reply_to(message, translate(msg))


tarjimonbot.polling()
