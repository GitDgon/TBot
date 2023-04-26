import telebot

TOKEN = None



with open('token.txt') as f:
    TOKEN = f.read().strip()

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(messege):
    bot.send_message(messege.chat.id, '<b>Привет!</b>', parse_mode='html')




bot.polling(none_stop=True)