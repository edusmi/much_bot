# much_bot
Bot for Telegram.

Бот-акинатор, помогающий определить, какой гриб Вы сейчас держите в руках\нашли в лесу\задумали в голове. 
Информация о грибах хранится в коде в виде списка (ибо на Heroku нормально устанавливаться база данных отказалась), 
алгоритм основывается на реализации дерева решений (не бинарного):
задавая определенные вопросы и получая 1 из предложенных вариантов ответа как правильный, 
бот отсеивает лишнюю информацию о непопадающих под указанное условие грибах.
Это происходит до тех пор, пока он не определит, о каком грибе шла речь.
