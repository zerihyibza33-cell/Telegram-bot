import telebot

TOKEN = "8772785235:AAFn2OTEAQu_BYKhq-XKMbQBF3EoGpKh2CA"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Hello! I'm your bot 🤖")

bot.infinity_polling()
