##For this case i will going to use the pip method
##pip install pyTelegramBotAPI form this lib https://pypi.org/project/pyTelegramBotAPI/0.3.0/

import telebot

TOKEN = '<put in here your telegram token string>'
tbot = telebot.TeleBot(TOKEN)

#or you can use

tbot = telebot.TeleBot('<put in here your telegram token string>')

##for obtain a token, you need to read this link https://core.telegram.org/bots#6-botfather
