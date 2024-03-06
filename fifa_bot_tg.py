import random
import telebot

TOKEN = '7044382109:AAFxgXdSGR2I-mhOkzu0cwKUHNZHTY1hPPA'
bot = telebot.TeleBot(TOKEN)
pak1 = {'rikolord': None, 'VladislavB': 1, 'K_gretzkiy': None, 'Roman_meatuniverse': None, 'mkeyck': None}
pak2 = {'Jzxswim': None, 'SlavaBern': 1, 'ilya_rudnik': None, 'DM11ITRY': None, 'sokolov_artyom': None}


@bot.message_handler(commands=['list'])
def show_list(message):
    final_list = ''
    count = 0
    for name_pak1, number_pack_1 in pak1.items():
        for name_pak2, number_pack_2 in pak2.items():
            if ((type(number_pack_1) is int) and (type(number_pack_2) is int)) and number_pack_1 == number_pack_2:
                count += 1
                final_list = '\n'.join(
                    (final_list, ('Команда №' + str(count) + ' — ' + '@' + name_pak1 + ' + ' + '@' + name_pak2)))
    bot.send_message(message.chat.id, final_list)


@bot.message_handler(commands=['num'])
def show_num(message):
    flag = True
    if message.from_user.username in pak1.keys():
        if isinstance(pak1[message.from_user.username], int):
            refuse_text = f'@{message.from_user.username}, твой номер - {pak1[message.from_user.username]}!'
            bot.reply_to(message, refuse_text)
            exit()
        else:
            while flag:
                num = random.randint(1, 5)
                if num not in pak1.values():
                    pak1[message.from_user.username] = num
                    flag = False
                    count = 0
                    for none in pak1.values():
                        if none is None:
                            count += 1
                    if count == 0:
                        text_finish = f'Твой номер - {str(num)}! Все из корзины №1 выбрали номер!'
                        bot.reply_to(message, text_finish)
                    else:
                        text = f'Твой номер - {str(num)}! Осталось {str(count)} человека без номера в корзине №1!'
                        bot.reply_to(message, text)
                else:
                    continue
    elif message.from_user.username in pak2.keys():
        if isinstance(pak2[message.from_user.username], int):
            refuse_text = f'@{message.from_user.username}, твой номер - {pak2[message.from_user.username]}!'
            bot.reply_to(message, refuse_text)
            exit()
        else:
            while flag:
                num = random.randint(1, 5)
                if num not in pak2.values():
                    pak2[message.from_user.username] = num
                    flag = False
                    count = 0
                    for none in pak2.values():
                        if none is None:
                            count += 1
                    if count == 0:
                        text_finish = f'Твой номер - {str(num)}! Все из корзины №2 выбрали номер!'
                        bot.reply_to(message, text_finish)
                    else:
                        text = f'Твой номер - {str(num)}! Осталось {str(count)} человека без номера в корзине №2!'
                        bot.reply_to(message, text)
                else:
                    continue
    else:
        absence_text = "Извини, тебя нет ни в одной из корзин!"
        bot.reply_to(message, absence_text)


bot.polling(none_stop=True)
# Добавить команды. Словарь сильных и словарь слабых. Ключ-сильный игрок, значение - лист из сильной и слабой команды.
