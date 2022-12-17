from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from random import randint

from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

emoj = '❤️⚡️😘👍🔥💩💪🏿👈🏿👈🏿💯🤙🏿😎☺️☎️😣🚶🎉🎲🥲🥲☺️😍😊🐱😍😋🥳☹️🙁🥶😨😮🥱☠️👹😈💪🏿🫂🗣👅👳🏻‍♂️👩🏿‍⚕️👝👟🐱🙉🐔🦆🪱🐛🐴🐣🐍🦖🐊🦏🦔🍀🎍🎋🌛🌕🌍⭐️💧🍈🥝🍍🧄🥔🍖🍔🍰🥧🥛🍵🧂🏓🏓🏒🛹🤼🏋🏼‍♂️🪘🎪🚠🚝🚉⚓️🏯🎢'


@dp.message_handler(commands=['start'])
async def hello_mes(message: types.Message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    item_1 = types.KeyboardButton("/help")
    item_2 = types.KeyboardButton("/help_сhat")
    item_3 = types.KeyboardButton("/info")
    markup.add(item_1, item_2, item_3)
    await bot.send_message(message.chat.id, "Саламулейкум дорогой друг,"

                                            "\n нажми на кнопку help, чтобы узнать команды "
                                            "\n нажми на кнопку help_chat, чтобы узнать возможности в чате "
                                            "\n нажми info, что посмотреть возможности",
                           reply_markup=markup)


@dp.message_handler(commands=['info'])
async def information(message):
    text = '''Этого бота можно добавить в чат, чтобы управлять им он может 
    (1)приветстовать новых пользователь, 
    (2) выходить из чата, 
    (3) выводить инфу по участникам и админам
    
    бот также может 
    (4)выдать рандомный смайлик, 
    (5) рассказать про кота, 
    (6) отправить фотокарточку выбранного кота'''
    await bot.send_message(message.chat.id, text)

@dp.message_handler(commands=['help'])
async def help(message):
    text = '''
/start - начать 
/get_random_emoji
/cat - фотки мурок
/info - про возможности
/help - команды
/help_chat - команды по чату по чату
    '''
    b1 = types.KeyboardButton("/start")
    b2 = types.KeyboardButton("/cat")
    b3 = types.KeyboardButton("/get_random_emoji")
    b4 = types.KeyboardButton("/help_chat")
    b5 = types.KeyboardButton("/help")
    b6 = types.KeyboardButton("/info")
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    markup.add(b1, b2, b3, b4, b5, b6)
    await bot.send_message(message.chat.id, text, reply_markup=markup)


@dp.message_handler(commands=['help_chat'])
async def help_chat(message):
    text = '''
Этого бота можно добалять в чат, чтобы немного управлять им

напиши "Выйди из чата" - бот покинет чат

напиши "Статистика по чату" - бот выдаст статистику по чату

/ban - ответь этим на сообщение того, кого забанить(не должен быть админом)
/start - начать 
/help - команды
/help_chat - информация по чату
    '''
    b1 = types.KeyboardButton("Выйди из чата")
    b2 = types.KeyboardButton("Статистика по чату")
    b3 = types.KeyboardButton("/ban")
    b4 = types.KeyboardButton("/help_chat")
    b5 = types.KeyboardButton("/help")
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    markup.add(b1, b2, b3, b4, b5)
    await bot.send_message(message.chat.id, text, reply_markup=markup)

@dp.message_handler(commands=['cat'])
async def cat(message):
    b1 = types.KeyboardButton("Серый")
    b2 = types.KeyboardButton("Рыжий")
    b3 = types.KeyboardButton("Черный")
    b4 = types.KeyboardButton("Белый")
    b5 = types.KeyboardButton("/help")
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    markup.add(b1, b2, b3, b4, b5)
    text = '''
    Мейн-кун – аборигенная порода американских кошек, 
характеризующаяся крупными размерами и внушительной массой тела. Представители 
породы – это надежные друзья и компаньоны, способные быстро завоевать любовь всей семьи.'''
    await bot.send_message(message.chat.id, text, reply_markup=markup)

@dp.message_handler(commands=['get_random_emoji'])
async def rd(message):
    r = randint(0, len(emoj) - 1)
    text = emoj[r]
    await bot.send_message(message.chat.id, text)

@dp.message_handler(content_types=['new_chat_members'])
async def hey(message):
    await bot.send_message(message.chat.id, "Саламулейкум дорогой друг")

@dp.message_handler(commands=["ban"])
async def ban_user(message):
    try:
        await bot.kick_chat_member(message.chat.id, message.reply_to_message.from_user.id)
        await bot.send_message(message.chat.id, "done")
    except Exception as e:
        await bot.send_message(message.chat.id, e)
        await bot.send_message(message.chat.id, 'ответьте на сообщение осужденного')
        await bot.send_message(message.chat.id, 'он не должен быть админом')

@dp.message_handler(content_types=['text'])
async def message_reply(message):
    if message.text == 'Чурка' or message.text == 'Хач':
        await bot.send_message(chat_id=message.chat.id, text='сам ты ' + message.text)

    if message.text == 'Выйди из чата':
        await bot.leave_chat(message.chat.id)

    if message.text == 'Статистика по чату':
        users = await bot.get_chat_member_count(message.chat.id)
        admins = len(await bot.get_chat_administrators(message.chat.id))
        text = f'пользователей в чате: {users} \nадминов в чате: {admins}'

        await bot.send_message(message.chat.id, text)
    if message.text == 'Серый':
        cat_1 = 'https://krasivosti.pro/uploads/posts/2021-06/1623483458_6-krasivosti_pro-p-mein-kun-serii-zhivotnie-krasivo-foto-6.jpg'
        await bot.send_photo(message.chat.id, cat_1)

    if message.text == 'Рыжий':
        cat_2 = 'https://oir.mobi/uploads/posts/2021-05/1621494979_12-oir_mobi-p-mein-kun-rizhii-bolshoi-zhivotnie-krasivo-14.jpg'
        await bot.send_photo(message.chat.id, cat_2)

    if message.text == 'Черный':
        cat_3 = 'https://funart.pro/uploads/posts/2021-07/1627509133_3-funart-pro-p-chernie-mein-kuni-zhivotnie-krasivo-foto-3.jpg'
        await bot.send_photo(message.chat.id, cat_3)

    if message.text == 'Белый':
        cat_4 = 'https://funart.pro/uploads/posts/2021-07/1626890244_10-funart-pro-p-belii-mein-kun-s-golubimi-glazami-zhivotni-12.jpg'
        await bot.send_photo(message.chat.id, cat_4)

# -------------------------------------
if __name__ == '__main__':
    executor.start_polling(dp)
