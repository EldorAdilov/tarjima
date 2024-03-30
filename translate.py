from googletrans import Translator


def translate(text):
    translator = Translator()
    til = translator.detect(text).lang
    if til == 'en':
        return translator.translate(text, dest='uz').text
    else:
        return translator.translate(text, dest='en').text
