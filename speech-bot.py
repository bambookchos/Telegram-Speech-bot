# -*- coding: utf-8 -*-
import telebot
token = 'BOT_TOKEN'
bot = telebot.TeleBot(token)
from gtts import gTTS
import os
import sys
import datetime

reload(sys)
sys.setdefaultencoding('utf8')



last =[]

@bot.message_handler(commands=['sina'])
def sina(message):
    os.system("omxplayer sounds/sina.mp3")

@bot.message_handler(commands=['vunderkind'])
def vunderkind(message):
    os.system("omxplayer sounds/vunderkind.mp3")

@bot.message_handler(commands=['shortsina'])
def shortsina(message):
    os.system("omxplayer sounds/sina2.mp3")

@bot.message_handler(commands=['ktosuka'])
def ktosuka(message, last_u = last):
    now = datetime.datetime.now()
    msg = ""
    for i in last_u:
        diff = now - i[1]
        if int(diff.total_seconds() / 60) < 5:
            msg += i[1].strftime("%Y-%m-%d %H:%M:%S")+" "+i[0]+"\n"
    bot.send_message(message.chat.id, msg)


@bot.message_handler(content_types=["text"])
def repeat_all_messages(message, last_u = last):
    tts = gTTS(text=message.text, lang='ru')
    tts.save("temp.mp3")
    os.system("mpg321 -g 1000 temp.mp3")
    last_u.append([message.from_user.username, datetime.datetime.now()])




if __name__ == '__main__':
     bot.polling(none_stop=True)
