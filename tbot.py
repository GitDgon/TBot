import telebot
import webbrowser
import datetime
import threading

TOKEN = None
with open('token.txt') as f:
    TOKEN = f.read().strip()

bot = telebot.TeleBot(TOKEN)
users = {}
print(type(users))
print(users)


@bot.message_handler(commands=['start'])
# декоратор message_handler, он позволяет сообщить телеграму какую команду мы отслеживаем (сама команда передаётся в списке commands)
def welcom(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, 'Добрый день! Введи имя!')
    users[chat_id] = {}
    print(users)
    # register_next_step_handler - функция позволяющая задать следующий шаг бота
    # В этой функции мы указываем два аргумента:
    # message - основной объект в телеграм ботах,
    # который содержит всю необходимую информацию (id чата, текст сообщения и тд), а также ссылка на функцию, которая будет далее вызываться.
    bot.register_next_step_handler(message, save_username)

def save_username(message):
    chat_id = message.chat.id
    name = message.text
    users[chat_id]['name'] = name
    print(users)
    bot.send_message(chat_id, f'{name}, Укажи фамилию!')
    bot.register_next_step_handler(message, save_surname)

def save_surname(message):
    chat_id = message.chat.id
    surname = message.text
    users[chat_id]['surname'] = surname
    name = users[chat_id]['name']

    print(users)
    bot.send_message(chat_id, f'{surname} {name}, вы зарегистрированы!')  #(users[chat_id]['name']))
    #bot.register_next_step_handler(message, save_surname())


@bot.message_handler(commands=['whomy'])
def whomy(message):
    chat_id = message.chat.id
    surname = users[chat_id]['surname']
    name = users[chat_id]['name']
    bot.send_message(chat_id, f'Вы: {name} {surname}')








@bot.message_handler(commands=['site', 'web'])
def site(massage):
    webbrowser.open('https://www.mail.ru')


@bot.message_handler(commands=['test'])
def start(message):
    print(message.chat.id)


@bot.message_handler(commands=['ping'])
def command(message):
    baner = str('pingtest')
    chat_id = -1002654832876

    print(type(chat_id))
    print(chat_id)
    bot.send_message(chat_id, f'Проверка: {baner}')


@bot.message_handler(commands=['date'])
def start(message):
    print(message.from_user.username)
    print(message.chat.id)
    if message.from_user.username is None:
        bot.send_message(message.chat.id, f'Привет, {message.from_user}')
        # bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name} {message.from_user.language_code}')
    else:
        bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name} {message.from_user.username}')


@bot.message_handler(commands=['help'])
def start(message):
    bot.send_message(message.chat.id, '<b>Привет!</b>', parse_mode='html')


@bot.message_handler()
def info(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name} {message.from_user.language_code}')
    elif message.text.lower() == '/id':
        bot.reply_to(message, f'ID: {message.from_user.id}')

# if __name__ == '__main__':
#     print('Бот запущен!')
    # bot.infinity_polling(none_stop=True)
bot.polling(none_stop=True)
