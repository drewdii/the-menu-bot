# easier to understand python scripts
# main dependenciy = pyTelegramBotAPI

import os
import telebot

API_KEY = os.getenv('API_KEY')
bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['greet'])
def greet(message): 
    bot.reply_to(message, "Hey, how is it going?")

@bot.message_handler(commands=['hello'])
def hello(message):
    bot.send_message(message, "Hello!")

bot.polling()


