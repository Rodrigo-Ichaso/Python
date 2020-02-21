#For this case i will going to use the pip method
#pip install pyTelegramBotAPI 
#from this lib https://pypi.org/project/pyTelegramBotAPI/0.3.0/

import telebot

TOKEN = '<put in here your telegram token string>'
tbot = telebot.TeleBot(TOKEN)

#or you can use

tbot = telebot.TeleBot('<put in here your telegram token string>')
