import telebot
import webbrowser

TOKEN = None
with open('token.txt') as f:
    TOKEN = f.read().strip()

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['site', 'web'])
def site(massage):
    webbrowser.open('https://www.mail.ru')




@bot.message_handler(commands=['start'])
def start(message):
    print(message.from_user.username)
    if message.from_user.username is None:
        bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name} {message.from_user.language_code}')
    else:
        bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name} {message.from_user.username}')



@bot.message_handler(commands=['help'])
def start(message):
    bot.send_message(message.chat.id, '<b>Привет!</b>', parse_mode='html')


@bot.message_handler()
def info(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name} {message.from_user.language_code}')
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'ID: {message.from_user.id}')


bot.polling(none_stop=True)