import telebot
import random
import string
import webbrowser
import time
from telebot import types
from config import TOKEN
bot = telebot.TeleBot(TOKEN)






@bot.message_handler(commands=['сайт'])
def site(message):
    bot.send_message(message.chat.id, 'сайт не готов, ждите еще')


@bot.message_handler(commands=['css'])
def css2(message):
 css = types.InlineKeyboardMarkup()
 css.add(types.InlineKeyboardButton('что такое css', callback_data='css3'))
 bot.send_message(message.chat.id, 'нажмите, чтобы узнать ответ ', reply_markup=css)





@bot.message_handler(commands=['question', 'que'])
def q(message):
    bot.send_message(message.chat.id, 'какой вопрос вас интересует?:')
    k9 = types.InlineKeyboardMarkup()
    k9.add(types.InlineKeyboardButton('когда будут новые обновления для бота?', callback_data='a1'))
    k9.add(types.InlineKeyboardButton('какой у тебя будет следующий проект?', callback_data='a2'))
    bot.send_message(message.chat.id, 'нажми на интересующий тебя вопрос', reply_markup=k9)




@bot.message_handler(commands=['hex'])
def hex(message):
    pas = ''.join(random.choice(string.hexdigits) for i in range(116))
    bot.send_message(message.chat.id, f'ваш hex: {pas}'),





@bot.message_handler(commands=['random_password', 'pas'])
def random_password(message):
    password1 = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for i in range(20))
    password2 = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for i in range(20))
    bot.send_message(message.chat.id, f'Ваш первый случайный пароль: {password1}')
    bot.send_message(message.chat.id, f'Ваш второй случайный пароль: {password2}')





@bot.message_handler(commands=['resources'])
def resource(message):
    bot.send_message(message.chat.id,
                     'вот некоторые ресурсы, которые могут быть полезными: https://github.com/romanvht/ByeDPIAndroid/releases/tag/v.1.4.0 - обход блокировок по dpi для мобилок \n https://github.com/Flowseal/zapret-discord-youtube - обход блокировки дискорд и ютуб для пк \n https://github.com/ValdikSS/GoodbyeDPI - обход блокировок по dpi для пк')
    a = types.InlineKeyboardMarkup()
    a.add(types.InlineKeyboardButton('предупреждение', callback_data='danger'))
    bot.send_message(message.chat.id, 'важная информация', reply_markup=a)


@bot.message_handler(commands=['important', 'impo', 'Gpt'])
def ends(message):
    bot.send_message(message.chat.id, 'дополнительно')
    dec = types.InlineKeyboardMarkup()
    dec.add(types.InlineKeyboardButton('спасибо за пояснения, жду Chat Gpt', callback_data='add'))
    dec.add(types.InlineKeyboardButton('Chat Gpt', callback_data='add2'))
    dec.add(types.InlineKeyboardButton('нажмите, чтобы перейти на мой ресурс', callback_data='add3'))
    dec.add(types.InlineKeyboardButton('что из себя представляет DPI?', callback_data='add4'))
    bot.send_message(message.chat.id, 'дополнительно:', reply_markup=dec)







@bot.message_handler(commands=['bridges'])
def br(message):
    bot.send_message(message.chat.id, 'мосты для tor: obfs4 15.235.48.110:6241 16AE419DBE20765A30E27008E1359DBDBAD260E1 cert=gRpsUldyaLSeBI51nMWcu55dwdD8YJ0N6DQJZxugFS995I+c24PtAaJVy1sfc+fnTvZcGQ iat-mode=0 ')
    bri = types.InlineKeyboardMarkup()
    bri.add(types.InlineKeyboardButton('предупреждение', callback_data='briges1'))
    bot.send_message(message.chat.id, 'важная информация!!!', reply_markup=bri)


@bot.message_handler(commands=['DS, Ds, dS, Ds', 'ds'])
def ds(message):
    url = 'https://discord.gg/GKAyztMa'
    bot.send_message(message.chat.id, f'Ссылка на дискорд сервер {url}')




@bot.message_handler(commands=['ass'])
def nas(message):
    url = 'https://www.youtube.com/'
    bot.send_message(message.chat.id, f'вот ссылка на данный ресурс: {url}')






@bot.message_handler(commands=['спасибо'])
def message(message):
    bot.send_message(message.chat.id, 'пожалуйста, рад был помочь вам')
    site2 = types.InlineKeyboardMarkup()
    site2.add(types.InlineKeyboardButton('GitHub', callback_data='site'))
    site2.add(types.InlineKeyboardButton('Youtube', callback_data='You'))
    btw = site2.add(types.InlineKeyboardButton('Discord', callback_data='discord'))
    bot.send_message(message.chat.id, 'ваше действие', reply_markup=site2)




@bot.message_handler(content_types=['photo'])
def ass(message):
    ass = types.InlineKeyboardMarkup()
    ass.add(types.InlineKeyboardButton('перейти на сайт ', url='https://sites.google.com/?hl=RU'))
    ass.add(types.InlineKeyboardButton('удалить фото', callback_data='delete'))
    ass.add(types.InlineKeyboardButton('редактировать текст', callback_data='edit'))
    bot.reply_to(message, 'какое красивое фото, мне нравится', reply_markup=ass)




@bot.message_handler(commands=['rate'])
def soo(message):
    bot.send_message(message.chat.id, 'дайте свою оценку')
    count = types.InlineKeyboardMarkup()
    count.add(types.InlineKeyboardButton('да', callback_data='mess'))
    count.add(types.InlineKeyboardButton('нет', callback_data='mess2'))
    bot.send_message(message.chat.id, 'вам нравится этот бот?', reply_markup=count )



@bot.message_handler(commands=['help', 'Help'])
def message2(message):
    bot.send_message(message.chat.id, 'кто вам нужен')
    moderate = types.InlineKeyboardMarkup()
    moderate.add(types.InlineKeyboardButton('модерация', callback_data='moderation'))
    moderate.add(types.InlineKeyboardButton('служба поддержки бота', callback_data='help'))
    bot.send_message(message.chat.id, 'список служб, куда вы можете обратится', reply_markup=moderate)


@bot.callback_query_handler(func= lambda call: True)
def func(callback):
    moder = callback.message.chat.id
    if callback.data == 'moderation':
        bot.send_message(callback.message.chat.id, 'поиск свободного модератора...')
        time.sleep(4)
        bot.send_message(callback.message.chat.id, 'напишите модератору @pornstar228007')


    elif callback.data == 'help':
        bot.send_message(callback.message.chat.id, 'ищем свободного помощника...')
        time.sleep(4)
        bot.send_message(callback.message.chat.id, 'напишите помощнику @pornstar228007')
    elif callback.data =='mess':
        bot.send_message(callback.message.chat.id, 'спасибо за высокую оценку, я буду развивать бота дальше')
    elif callback.data == 'mess2':
        bot.send_message(callback.message.chat.id, 'ничего страшного что вам не понравился мой бот, он еще довольно сырой, но через время он станет куда лучше чем сейчас)')
    if callback.data == 'edit':
        bot.edit_message_text('текст был изменен', callback.message.chat.id, callback.message.message_id)
    elif callback.data == 'delete':
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)
    elif callback.data == 'escape':
        bot.send_message(callback.message.chat.id, 'дата глобального запуска бота еще неизвестна, бот еще сыроватый и не готов для запуска')
    elif callback.data == 'cum':
        bot.send_message(callback.message.chat.id, 'его основаная проблема это урезанность, бот достаточно урезан в своем функционале, надеюсь в скором времени его функционал расширится')
    elif callback.data == 'what':
        bot.send_message(callback.message.chat.id, 'никаких проблем с интеграцией Chat Gpt нет, он может быть добавлен в любой момент времени, но я хочу добавить в бота команды для обратной связи, чтобы вы могли сообщить о каких либо проблемах связанных с ботом, Chat Gpt будет но пока не на этом этапе')
    elif callback.data == 'add':
        bot.send_message(callback.message.chat.id, 'отлично, спасибо что не покидаете и следите за моим проектом')
    elif callback.data == 'add2':
        bot.send_message(callback.message.chat.id, 'недоступно, дата релиза Chat Gpt - неизвестна')
    elif callback.data == 'add3':
        bot.send_message(callback.message.chat.id, 'вы будете перемещены на ресурс через: 5')
        time.sleep(1)
        bot.send_message(callback.message.chat.id, '4')
        time.sleep(1)
        bot.send_message(callback.message.chat.id, '3')
        time.sleep(1)
        bot.send_message(callback.message.chat.id, '2')
        time.sleep(1)
        bot.send_message(callback.message.chat.id, '1...')
        time.sleep(4)
        bot.send_message(callback.message.chat.id, 'перемещение...')
        time.sleep(4)
        webbrowser.open('https://youtu.be/xvFZjo5PgG0')
    elif callback.data == 'briges1':
        bot.send_message(callback.message.chat.id, 'если вы используете браузер тор то будьте осторожными, не давайте свою личную информацию никому(эп, пароли, логины и тд), тор браузер запрещен за территории рф, будьте очень бдительными, на сегодняшний день мост актуален, если у вас не будет работать данный мост, напишите мне лс, выдам вам новый мост, личка: @cooked228. К огромному сожалению мосты автоматически приходить сюда не смогут, так как у меня нет доступа к API тор браузер, извините, если новые мосты будут приходить с задержкой. ')
    elif callback.data == 'danger':
        bot.send_message(callback.message.chat.id, 'все эти ресурсы, которые были показаны являются средством обхода блокировок с открытым исходным кодом, поэтому переживать за свои данные я думаю незачем, на данный момент времени все эти обходы могут работать не везде и не у всех провайдеров, этому есть причина, она заключается в том что сейчас ркн может банить ip не как раньше что от этого страдали почти все, сейчас они могут бить точечно и блокировать конкретные популярные ip адреса, полягли многие впн сервисы как раз поэтому, ркн точечно бьет по серверам и соответственно до них не достучаться, и примерно тоже самое происходит и со всеми обходами блокировок, коректная работа может зависить от ip адреса на котором вы сидите, может завиисить от dns сервера, и есть такая практика что роскомнадзор блокируют ip диапазоны, ну и конечно сама географическая принадлежность, тоже один из факторов, те у кого обходы работают тем просто повезло с ip, либо еще с какими то факторами которые я перечислил, сто процентного способа обхода блокировок нет это и так понятно, едва ли ркн нравится вся эта шумиха с goodbyedpi и аналогами, поэтому их блокировка это лишь вопрос времени')
    elif callback.data == 'add4':
        bot.send_message(callback.message.chat.id, 'DPI - Deep Package Inspecton или же глубокий анализатор пакетов, представляет из себя можно так сказать цифровую томожню, которая как раз и поволяет пройти трафику определенного ресурса, а какой то трафик она не пропускает, так же и действует ркн при замедении ютуб, эту блокировку можно легко обойти при помощи способов, которые я указал в команде /resources')
    elif callback.data == 'site':
        webbrowser.open('https://github.com/')
    elif callback.data == 'You':
        webbrowser.open('https://www.youtube.com/')
    elif callback.data == 'discord':
        webbrowser.open('https://discord.com/')
    elif callback.data == 'a1':
        bot.send_message(callback.message.chat.id, 'обновлений для бота пока что не предвидится, я щас работаю над другим проектом, который меня заинтересовал, обновления пока что не будут выходить, но иногда будут какие либо апдейты, не знаю когда выйдет патч но надеюсь скоро')
    elif callback.data == 'a2':
        bot.send_message(callback.message.chat.id, 'основной проект, которым я щас занимаюсь это сайт, я одновременно и изучаю построение сайтов, и одновременно со своим обучением сайт разрабатываю, пока что этот сайт очень сырой, там нет никакой юзабельности ну и соответственно коммуникации с пользователями, когда сайт будет готов дам вам всем знать')
    elif callback.data == 'css3':
        bot.send_message(callback.message.chat.id, 'CSS — это язык описания внешнего вида документа, то есть он отвечает за то, как выглядят веб-страницы: цвет фона и декоративных элементов, размер и стиль шрифтов. Термин расшифровывается как Cascading Style Sheets (каскадные таблицы стилей).')







@bot.message_handler(commands=['my_profile'])
def message(message):
     user = message.from_user
     bot.reply_to(message, f'вот информация о вас: {user.first_name}, ваш id: {user.id}')








@bot.message_handler(commands=['fullfunc'])
def message(message):
    bot.send_message(message.chat.id, 'функции которые есть в боте, новые функции которые будут добавлены они будут в /func, бот может похвастаться обработчиком команд /start, так же введя команду /help бот скажет вам привет и назовет вас по имени, остальной функционал бота я уже перечислил в /func, если вам и правда интересен мой проект то перейдите на мой ютуб канал введя команду /site')





@bot.message_handler(commands=['привет', 'start', 'hi', 'Hi', 'sup', 'Sup'])
def message(message):
    bot.send_message(message.chat.id, 'Это пре-альфа версия бота, функционал еще урезанный и со временем что то будет добавляться но и убираться, в планах убрать несколько команд от которых нет никакого смысла, надеюсь в скором времени выкачу этот апдейт, в будущем будет поддержка Chat Gpt!, если хотите узнать какие команды есть у бота кликните на /fullfunc если вы хотите следить за развитием проекта то переходите на мой ютуб канал используя команду /site PS: я смог восстановить доступ к телеграм боту, было на то несколько причин, но сейчас все работает)')






@bot.message_handler(commands=['site', 'website'])
def site(message4):
    webbrowser.open('https://youtu.be/xvFZjo5PgG0?si=BFEWomOK5CqD2Svv')



bot.infinity_polling()