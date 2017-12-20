import telebot
import config
from itertools import groupby


bot = telebot.TeleBot(config.token)
sor1 = []
sor2 = []
sor3 = []
sor4 = []
sor5 = []
lts = [['Боровик', 1, 'Розовато-красная', 'Выпуклая', 'Утолщенная', 'Буро-оливковый', 'Желтая'],
       ['Белый гриб', 1, 'Темно-коричневая', 'Полушаровидная', 'Раздутая', 'Оливково-зеленый', 'Белая'],
       ['Валуй', 1, 'Желтая', 'Шаровидная', 'Бочонковидная', 'Кремовый', 'Белая'],
       ['Волнушка', 1, 'Розовато-красная', 'Выпуклая', 'Цилиндрическая', 'Белый', 'Белая'],
       ['Груздь', 1, 'Белая', 'Воронковидная', 'Цилиндрическая', 'Желтый', 'Белая'],
       ['Дубовик', 1, 'Желтовато-коричневая', 'Полушаровидная', 'Булавовидная', 'Оливково-бурый', 'Желтая'],
       ['Лисичка', 1, 'Оранжево-желтая', 'Воронковидная', 'Сросшаяся', 'Желтый', 'Светло-желтая'],
       ['Масленок', 1, 'Шоколадно-буроватая', 'Выпуклая', 'Цилиндрическая', 'Бурый', 'Буро-желтая'],
       ['Опенок', 1, 'Серо-желтая', 'Шаровидная', 'Цилиндрическая', 'Белый', 'Белая'],
       ['Подберезовик', 1, 'Темно-коричневая', 'Полушаровидная', 'Цилиндрическая', 'Оливково-бурый', 'Белая'],
       ['Подосиновик', 1, 'Красно-оранжевая', 'Шаровидная', 'Сплошная', 'Желто-бурый', 'Бело-серая'],
       ['Рыжик', 1, 'Рыжая', 'Воронковидная', 'Цилиндрическая', 'Оранжевый', 'Оранжевая'],
       ['Сыроежка', 1, 'Розовато-коричневая', 'Плоско-выпуклая', 'Цилиндрическая', 'Белый', 'Белая'],
       ['Шампиньон', 1, 'Белая', 'Полушаровидная', 'С двухслойным кольцом', 'Пурпурно-коричневый', 'Белая'],
       ['Бледная поганка', 0, 'Желтовато-буро-оливковая', 'Плоско-выпуклая', 'С кольцом', 'Белый', 'Белая'],
       ['Мухомор', 0, 'Красная', 'Плоско-выпуклая', 'Цилиндрическая', 'Белый', 'Белая'],
       ['Ложноопенок', 0, 'Желто-бурая', 'Распростертая', 'Волокнистая', 'Шоколадно-коричневый', 'Светло-желтая'],
       ['Шампиньон рыжеющий', 0, 'Желтовато-белая', 'Колокольчатая', 'С двухслойным кольцом', 'Темно-коричневый', 'Бурая'],
       ['Энтолома ядовитая', 0, 'Серо-бурая', 'Распростертая', 'Согнутая', 'Розовый', 'Белая'],
       ['Рядовка ядовитая', 0, 'Грязно-белая', 'Распростертая', 'Цилиндрическая', 'Белый', 'Серая'],
       ['Ложнодождевик', 0, 'Грязно-желтая', 'Клубневидная', 'Отсутствует', 'Оливково-бурый', 'Оливково-бурая'],
       ['Бьеркандера дымчатая', 0, 'Бурая', 'Клубневидная', 'Отсутствует', 'Кремовый', 'Желто-бурая'],
       ['Свинушка', 0, 'Охристо-бурая', 'Воронковидная', 'Цилиндрическая', 'Бурый', 'Желтая'],
       ['Чешуйница', 0, 'Бежевая', 'Колокольчатая', 'Тонкая', 'Белый', 'Рыже-коричневая'],
       ['Серушка', 0, 'Коричневато-свинцовая', 'Воронковидная', 'Цилиндрическая', 'Белый', 'Белая'],
       ['Лисичка ложная', 0, 'Оранжево-желтая', 'Воронковидная', 'Согнутая', 'Желтый', 'Желтая'],
       ['Коллибия', 0, 'Рыжевато-коричневая', 'Ширококоническая', 'Цилиндрическая', 'Белый', 'Белая'],
       ['Перечный гриб', 0, 'Коричневая', 'Плоско-выпуклая', 'Цилиндрическая', 'Желто-бурый', 'Желтая']]


@bot.message_handler(commands=['start'])
def start(message):
    sent = bot.send_message(message.chat.id, 'Как тебя зовут?')
    bot.register_next_step_handler(sent, hello)


def hello(message):
    bot.send_message(message.chat.id, 'Привет, {name}. Рад тебя видеть.'.format(name=message.text))
    bot.send_message(message.chat.id, 'Сейчас я попробую определить, какой гриб тебя интересует.'.format(name=message.text))
    bot.send_message(message.chat.id, 'Но для этого тебе придется ответить на некоторые мои вопросы. Ты готов(а)?'.format(name=message.text))


@bot.message_handler(content_types=['text'])
def ready(message):

    if message.text == 'Да':
        rd(message)
    if message.text == 'Нет':
        bot.send_message(message.chat.id, 'Окей, всего доброго, пупс.')
        if message.text == '/start':
            start(message)


def exp(message):
    if message.text == 'Да':
        rd(message)
    elif message.text == 'Нет':
        ready(message)


def rd(message):
    bot.send_message(message.chat.id, 'Выберите и введите, какой формы шляпка у гриба:')
    lt = [] * len(lts)
    for i in range(len(lts)):
        lt.append([lts[i][3]])
    lt.sort()
    new_x = [el for el, _ in groupby(lt)]
    for i in range(len(new_x)):
        bot.send_message(message.chat.id, new_x[i])
    bot.register_next_step_handler(message, rd1)


def rd1(message):
    test1 = message.text
  #  bot.send_message(message.chat.id, test1)

    for i in range(len(lts)):
        tr = test1 in lts[i][3]
        if tr:
            sor1.append(lts[i])

    if len(sor1) == 1:

        bot.send_message(message.chat.id, 'Вы нашли: ' + str(sor1[0][0]))
        if sor1[0][1] == 0:
            bot.send_message(message.chat.id, 'Этот гриб несъедобен.')
            hot = bot.send_message(message.chat.id, 'Начинаем заново?')
            sor1.clear()

        else:
            bot.send_message(message.chat.id, 'Этот гриб съедобен.')
            hot = bot.send_message(message.chat.id, 'Начинаем заново?')
            sor1.clear()
        exp(hot)
    else:
        bot.send_message(message.chat.id, 'Выберите и введите, какого цвета шляпка гриба:')
        lt = [] * len(sor1)
        for i in range(len(sor1)):
            lt.append([sor1[i][2]])
        lt.sort()
        new_x = [el for el, _ in groupby(lt)]
        for i in range(len(new_x)):
            bot.send_message(message.chat.id, new_x[i])

        bot.register_next_step_handler(message, rd2)


def rd2(message):
    test2 = message.text
    #bot.send_message(message.chat.id, test1)

    for i in range(len(sor1)):
        tr = test2 in sor1[i][2]
        if tr:
            sor2.append(sor1[i])

    if len(sor2) == 1:

        bot.send_message(message.chat.id, 'Вы нашли: ' + str(sor2[0][0]))
        if sor2[0][1] == 0:
            bot.send_message(message.chat.id, 'Этот гриб несъедобен.')
            hot = bot.send_message(message.chat.id, 'Начинаем заново?')
            sor1.clear()
            sor2.clear()
        else:
            bot.send_message(message.chat.id, 'Этот гриб съедобен.')
            hot = bot.send_message(message.chat.id, 'Начинаем заново?')
            sor1.clear()
            sor2.clear()
        exp(hot)
    else:
        bot.send_message(message.chat.id, 'Выберите и введите, какого типа ножка гриба:')
        lt = [] * len(sor2)
        for i in range(len(sor2)):
            lt.append([sor2[i][4]])
        lt.sort()
        new_x = [el for el, _ in groupby(lt)]
        for i in range(len(new_x)):
            bot.send_message(message.chat.id, new_x[i])

        bot.register_next_step_handler(message, rd3)


def rd3(message):
    test1 = message.text

  #  bot.send_message(message.chat.id, test1)
    for i in range(len(sor2)):
        tr = test1 in sor2[i][4]
        if tr:
            sor3.append(sor2[i])

    if len(sor3) == 1:

        bot.send_message(message.chat.id, 'Вы нашли: ' + str(sor3[0][0]))
        if sor3[0][1] == 0:
            bot.send_message(message.chat.id, 'Этот гриб несъедобен.')
            hot = bot.send_message(message.chat.id, 'Начинаем заново?')
            sor1.clear()
            sor2.clear()
            sor3.clear()

        else:
            bot.send_message(message.chat.id, 'Этот гриб съедобен.')
            hot = bot.send_message(message.chat.id, 'Начинаем заново?')
            sor1.clear()
            sor2.clear()
            sor3.clear()
        exp(hot)
    else:
        bot.send_message(message.chat.id, 'Выберите и введите, какого цвета мякоть гриба:')

        lt = [] * len(sor1)
        for i in range(len(sor3)):
            lt.append([sor3[i][6]])
        lt.sort()
        new_x = [el for el, _ in groupby(lt)]
        for i in range(len(new_x)):
            bot.send_message(message.chat.id, new_x[i])

        bot.register_next_step_handler(message, rd4)


def rd4(message):
    test1 = message.text

 #   bot.send_message(message.chat.id, test1)

    for i in range(len(sor3)):
        tr = test1 in sor3[i][6]
        if tr:
            sor4.append(sor3[i])

    if len(sor4) == 1:

        bot.send_message(message.chat.id, 'Вы нашли: ' + str(sor4[0][0]))
        if sor4[0][1] == 0:
            bot.send_message(message.chat.id, 'Этот гриб несъедобен.')
            hot = bot.send_message(message.chat.id, 'Начинаем заново?')
            sor1.clear()
            sor2.clear()
            sor3.clear()
            sor4.clear()

        else:
            bot.send_message(message.chat.id, 'Этот гриб съедобен.')
            hot = bot.send_message(message.chat.id, 'Начинаем заново?')
            sor1.clear()
            sor2.clear()
            sor3.clear()
            sor4.clear()
        exp(hot)
    else:
        bot.send_message(message.chat.id, 'Выберите и введите, какого цвета споровый порошок гриба:')

        lt = [] * len(sor4)
        for i in range(len(sor4)):
            lt.append([sor4[i][5]])
        lt.sort()
        new_x = [el for el, _ in groupby(lt)]
        for i in range(len(new_x)):
            bot.send_message(message.chat.id, new_x[i])

        bot.register_next_step_handler(message, rd5)


def rd5(message):
    test1 = message.text

  #  bot.send_message(message.chat.id, test1)

    for i in range(len(sor4)):
        tr = test1 in sor4[i][5]
        if tr:
            sor5.append(sor4[i])

    if len(sor5) == 1:

        bot.send_message(message.chat.id, 'Вы нашли: ' + str(sor5[0][0]))
        if sor5[0][1] == 0:
            bot.send_message(message.chat.id, 'Этот гриб несъедобен.')
            hot = bot.send_message(message.chat.id, 'Начинаем заново?')
            sor1.clear()
            sor2.clear()
            sor3.clear()
            sor4.clear()
            sor5.clear()

        else:
            bot.send_message(message.chat.id, 'Этот гриб съедобен.')
            hot = bot.send_message(message.chat.id, 'Начинаем заново?')
            sor1.clear()
            sor2.clear()
            sor3.clear()
            sor4.clear()
            sor5.clear()
        exp(hot)


bot.polling()
