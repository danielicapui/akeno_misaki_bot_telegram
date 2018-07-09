# import os
# token = os.environ['610926090:AAGEAMy8wklAqjT04uZM2gfFJfO8GITUdqI'])
# export BOT_API_TOKEN="<610926090:AAGEAMy8wklAqjT04uZM2gfFJfO8GITUdqI>"
import os
import telepot
from Chatbot import Chatbot  
telegram = telepot.Bot('610926090:AAGEAMy8wklAqjT04uZM2gfFJfO8GITUdqI')

bot= Chatbot("Akeno_Misaki")

def recebendoMsg(msg):
    frase=bot.escuta(frase=msg['text'])
    resp= bot.pensa(frase)
    bot.fala(resp)
    #chatID= msg['chat']['id']
    tipoMsg, tipoChat, chatID= telepot.glance(msg)
    telegram.sendMessage(chatID,resp)

telegram.message_loop(recebendoMsg)

while True:
    pass


#@bot.message_handler(commands=['teste'])
#def comando_teste(mensagem):
 #    bot.reply_to(mensagem, 'Comando recebido')










# def recebendoMsg(msg):
    # frase = bot.escuta(frase=msg['text'])
    # resp = bot.pensa(frase)
    # bot.fala(resp)
    # chatID = msg['chat']['id']
    # tipoMsg, tipoChat, chatID = telepot.glance(msg)
    # telegram.sendMessage(chatID,resp)

# telegram.message_loop(recebendoMsg)

# while True:
    # pass