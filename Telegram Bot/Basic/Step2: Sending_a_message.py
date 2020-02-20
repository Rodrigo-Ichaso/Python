import telebot

tbot = telebot.TeleBot('put in here your telegram token string')
tbot.send_message(243432536, 'My First Telegram bot message')

#command used = tbot.send_message(chatid, message)
