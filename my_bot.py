import telebot
import random
import string

bot = telebot.TeleBot('7144256201:AAH-bnAzt6Tlilxyv1D6T3kTrelC-xCAtFs')

def generate_password(length):
  characters = string.ascii_letters + string.digits + string.punctuation
  password = ''.join(random.choice(characters) for i in range(length))
  return password


@bot.message_handler(commands=['start', 'hello'])
def main(message):
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}, этот бот поможет тебе придумать надежный пароль и расскажет, как защитить свои данные!')
    bot.send_message(message.chat.id, f'/start , /hello - бот поздоровается с вами и расскажет о имеющихся функциях:)\n/information - бот расскажет вам, кем был создан\n/security - бот расскажет вам, как защитить свои персональные данные при использовании мобильных устройств\n/password - бот придумает вам надёжный пароль для защиты ваших данных\n/end - бот попрощается с вами:)  ')

@bot.message_handler(commands=['end', 'Пока'])
def end(message):
    bot.send_message(message.chat.id, f'Хорошего дня, {message.from_user.first_name}!')

@bot.message_handler(commands=['information'])
def inform(message):
    bot.send_message(message.chat.id, f'Данный чат-бот создан студентами группы Б9123-01.03.02сп, Шариной Юлией и Егоровой Ириной')

@bot.message_handler(commands=['password'])
def info(message):
    bot.send_message(message.chat.id, f'Для начала введите количество символов в пароле.')
    @bot.message_handler()
    def password(message):
        try:
            password_length = int(message.text)
            password = generate_password(password_length)
            bot.send_message(message.chat.id,
                             f'Пароль сгенерирован: '
                             f'{password}'
                             )
            bot.send_message(message.chat.id,
                             f'Для генерации еще одного просто введите чило - длину пароля! Либо выберите 1 из команд: /start /information /security /end'
                             )

        except ValueError:
            return bot.send_message(message.chat.id, f'Введите только число для генерации пароля! Либо выберите нужную для вас команду:)')

@bot.message_handler(commands=['security'])
def security(message):
    bot.send_message(message.chat.id,
                     f'Соблюдение этих мер поможет уменьшить риск утечки вашей личной информации и защитит ваши данные на мобильном устройстве.\n'
                     f'1. Установите пароль или использование биометрической идентификации (например, сканер отпечатков пальцев или распознавание лица) для разблокировки устройства.\n'
                     f'2. Обновляйте операционную систему и приложения на вашем устройстве, чтобы исправлять уязвимости и обеспечить безопасность.\n'
                     f'3. Используйте надежные пароли или менеджеры паролей для хранения и управления вашими учетными данными.\n'
                     f'4. Ограничьте доступ к личной информации в приложениях, установив соответствующие настройки конфиденциальности.\n'
                     f'5. Избегайте подключения к ненадежным Wi-Fi сетям и используйте виртуальную частную сеть (VPN) при подключении к открытым сетям.\n'
                     f'6. Включите функцию удаленного управления устройством, чтобы удалить данные в случае утери или кражи.\n'
                     f'7. Будьте осторожны при скачивании приложений из сторонних источников - предпочтительнее использовать официальные магазины приложений, такие как App Store или Google Play.\n'
                     f'8. Не делитесь своими личными данными, такими как номер социального страхования, паспортные данные или банковские реквизиты, через ненадежные каналы связи или с незнакомыми людьми.')


bot.polling(none_stop=True)