import os
import telebot
bot = telebot.TeleBot('Token')


@bot.message_handler(content_types=['text'])
def start(message):
    bot.send_message(message.chat.id, "Здравствуйте, Вас приветствует бот технической поддержки. Какая у Вас фамилия, имя и отчество?")
    bot.register_next_step_handler(message, start1)

def start1(message):
    bot.send_message(message.from_user.id, 'В каком подразделении вы работаете?')
    file_path = 'D:/files/{0.first_name}'.format(message.from_user)+'{}'.format(message.from_user.id)+'.txt'
    if os.path.isfile(file_path) == True:
        doc = open('D:/files/{0.first_name}'.format(message.from_user) + '{}'.format(message.from_user.id)+'.txt','a')
    else:
        doc = open('D:/files/{0.first_name}'.format(message.from_user)+'{}'.format(message.from_user.id)+'.txt','w')
    doc.write("ФИО заявителя - {imia}\n".format(imia=message.text))
    doc.close()
    bot.register_next_step_handler(message, get_name)


def get_name(message):
    bot.send_message(message.from_user.id, 'Предоставьте пожалуйста ваш номер телефона и электронную почту?');
    doc = open('D:/files/{0.first_name}'.format(message.from_user)+'{}'.format(message.from_user.id)+'.txt','a')
    doc.write("Организация - {org}\n".format(org=message.text))
    doc.close()
    bot.register_next_step_handler(message, get_phone);


def get_phone(message):
    bot.send_message(message.from_user.id, 'Номер вашего кабинета?');
    doc = open('D:/files/{0.first_name}'.format(message.from_user)+'{}'.format(message.from_user.id)+'.txt','a')
    doc.write("Телефон - {phone}\n".format(phone=message.text))
    doc.close()
    bot.register_next_step_handler(message, get_cab);


def get_cab(message):
    bot.send_message(message.from_user.id, 'Опишите проблему?(Файлы не прикреплять)');
    doc = open('D:/files/{0.first_name}'.format(message.from_user)+'{}'.format(message.from_user.id)+'.txt','a')
    doc.write("Кабинет - {cabin}\n".format(cabin=message.text))
    doc.close()
    bot.register_next_step_handler(message, get_problem);


def get_problem(message):
    bot.send_message(message.from_user.id, 'Благодарим Вас за заявку. Если необходимо создать еще одну заявку, отправьте любое сообщение.');
    doc = open('D:/files/{0.first_name}'.format(message.from_user)+'{}'.format(message.from_user.id)+'.txt','a')
    doc.write("Проблема - {prob}\n".format(prob=message.text))
    doc.close()


bot.polling(none_stop=True, interval=0)
