import os
import telebot


bot = telebot.TeleBot("5211833757:AAGpCTbdqNVe87mCTd9qOtfJH1pvtHmovoA")


@bot.message_handler(commands=["start"])
def send_welcome(message):
  bot.reply_to(message, "Hello! I'm sharithma Chat Bot")


@bot.message_handler(commands=["how"])
def send_message(message):
  bot.send_message(message.chat.id, "https://youtube.com/c/sdmusicofficialyt")



bot.polling()
