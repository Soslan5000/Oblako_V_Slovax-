from config import TG_TOKEN
from config import TG_ANKETS_CHANNEL_ID
import telebot
from telebot import types
from murkups import markup_with_menu, markup_for_choise_form, markup_for_sizes, markup_for_sizes_after_final, \
    markup_for_county, markup_for_transitions_with_next, markup_for_transitions_with_pay, \
    markup_for_choise_form_after_final, markup_with_back, markup_for_commands
from murkups import menu_btn, back_btn, continue_btn, autor_btn, film_btn, serial_btn, painter_btn, poet_btn, \
    music_btn, game_btn, color_btn, book_btn, small_size_btn, medium_size_btn, big_size_btn, \
    return_btn, russia_btn, other_country_btn, edit_form_btn, edit_size_btn, pay_btn
from inline_kb import keyboard_for_links, keyboard_for_comment, keyboard_for_faq, keyboard_for_end
from messages import message_for_menu, message_for_about, message_for_links, \
    message_for_comment, thanks_for_the_order, message_for_FAQ, \
    message_for_more_info, message_for_except, message_for_notice
from classes import User
from other_functions import getRegData


bot = telebot.TeleBot(TG_TOKEN)
user_dict = {}


def send_menu(message):
    bot.send_message(message.chat.id,
                     message_for_menu,
                     reply_markup=markup_for_commands)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    try:
        bot.send_message(message.chat.id,
                         "Здравствуйте, " + message.from_user.first_name + '!\nНу что, приступим?' + message_for_menu,
                         reply_markup=markup_for_commands)
    except Exception as e:
        bot.reply_to(message, message_for_except, reply_markup=markup_with_menu)


@bot.message_handler(commands=['about'])
def send_about(message):
    try:
        msg = bot.send_message(message.chat.id,
                               message_for_about,
                               reply_markup=markup_with_menu)
        bot.register_next_step_handler(msg, menu)
    except Exception as e:
        bot.reply_to(message, message_for_except, reply_markup=markup_with_menu)


def menu(message):
    try:
        send_menu(message)
    except Exception as e:
        bot.reply_to(message, message_for_except, reply_markup=markup_with_menu)


@bot.message_handler(commands=['links'])
def send_links(message):
    try:
        bot.send_message(message.chat.id, message_for_links,
                               reply_markup=keyboard_for_links,
                               disable_web_page_preview=True)
        msg = bot.send_message(message.chat.id,
                               'Для возврата нажмите "В меню"',
                               reply_markup=markup_with_menu)
        bot.register_next_step_handler(msg, menu)
    except Exception as e:
        bot.reply_to(message, e, reply_markup=markup_with_menu)


def menu(message):
    try:
        send_menu(message)
    except Exception as e:
        bot.reply_to(message,
                     message_for_except,
                     reply_markup=markup_with_menu)


@bot.message_handler(commands=['faq'])
def FAQ(message):
    try:
        bot.send_message(message.chat.id,
                         message_for_FAQ,
                         reply_markup=keyboard_for_faq)
        msg = bot.send_message(message.chat.id,
                               'Для возврата нажмите "В меню"',
                               reply_markup=markup_with_menu)
        bot.register_next_step_handler(msg, menu)
    except Exception as e:
        bot.reply_to(message, message_for_except, reply_markup=markup_with_menu)


def menu(message):
    try:
        send_menu(message)
    except Exception as e:
        bot.reply_to(message, message_for_except, reply_markup=markup_with_menu)


@bot.message_handler(commands=['comment'])
def comment(message):
    try:
        bot.send_message(message.chat.id,
                         message_for_comment,
                         reply_markup=keyboard_for_comment)
        msg = bot.send_message(message.chat.id,
                               'Для возврата нажмите "В меню"',
                               reply_markup=markup_with_menu)
        bot.register_next_step_handler(msg, menu)
    except Exception as e:
        bot.reply_to(message, message_for_except, reply_markup=markup_with_menu)



def menu(message):
    try:
        send_menu(message)
    except Exception as e:
        bot.reply_to(message, message_for_except, reply_markup=markup_with_menu)


# /reg
@bot.message_handler(commands=["form"])
def start_form(message):
    try:
        msg = bot.send_message(message.chat.id,
                               'Выберите размер сюрприз бокса',
                               reply_markup=markup_for_sizes)
        bot.register_next_step_handler(msg, choise_form)
        user_dict[message.chat.id] = User()
    except Exception as e:
        bot.reply_to(message, message_for_except, reply_markup=markup_with_menu)


def choise_form(message):
    try:
        text = message.text
        chat_id = message.chat.id
        user = user_dict[chat_id]
        if text == big_size_btn or text == medium_size_btn or text == small_size_btn:
            user.size = message.text
            msg = bot.send_message(message.chat.id,
                                   'Выберите раздел и дайте нам знать, что Вам нравится больше всего',
                                   parse_mode="Markdown",
                                   reply_markup=markup_for_choise_form)
            bot.register_next_step_handler(msg, choise_rele)
        else:
            msg = bot.send_message(chat_id,
                                   'Ошибка. Воспользуйтесь кнопками для выбора размера',
                                   parse_mode="Markdown",
                                   reply_markup=markup_for_sizes)
            bot.register_next_step_handler(msg, choise_form)
    except Exception as e:
        bot.reply_to(message, message_for_except, reply_markup=markup_with_menu)


def choise_rele(message):
    try:
        chat_id = message.chat.id
        if message.text == autor_btn:
            msg = bot.send_message(chat_id,
                                   'Введите Вашего любимого автора',
                                   parse_mode="Markdown",
                                   reply_markup=types.ReplyKeyboardRemove())
            bot.register_next_step_handler(msg, autor_step, )
        elif message.text == film_btn:
            msg = bot.send_message(chat_id,
                                   'Введите Ваш любимый фильм',
                                   parse_mode="Markdown",
                                   reply_markup=types.ReplyKeyboardRemove())
            bot.register_next_step_handler(msg, film_step)
        elif message.text == serial_btn:
            msg = bot.send_message(chat_id,
                                   'Введите Ваш любимый сериал',
                                   parse_mode="Markdown",
                                   reply_markup=types.ReplyKeyboardRemove())
            bot.register_next_step_handler(msg, serial_step)
        elif message.text == painter_btn:
            msg = bot.send_message(chat_id,
                                   'Введите Вашего любимого художника',
                                   parse_mode="Markdown",
                                   reply_markup=types.ReplyKeyboardRemove())
            bot.register_next_step_handler(msg, painter_step)
        elif message.text == poet_btn:
            msg = bot.send_message(chat_id,
                                   'Введите Вашего любимого поэта',
                                   parse_mode="Markdown",
                                   reply_markup=types.ReplyKeyboardRemove())
            bot.register_next_step_handler(msg, poet_step)
        elif message.text == music_btn:
            msg = bot.send_message(chat_id,
                                   'Введите Вашу любимую музыкалькую группу',
                                   parse_mode="Markdown",
                                   reply_markup=types.ReplyKeyboardRemove())
            bot.register_next_step_handler(msg, music_group_step)
        elif message.text == game_btn:
            msg = bot.send_message(chat_id,
                                   'Введите Вашу любимую компьютерную игру',
                                   parse_mode="Markdown",
                                   reply_markup=types.ReplyKeyboardRemove())
            bot.register_next_step_handler(msg, game_step)
        elif message.text == color_btn:
            msg = bot.send_message(chat_id,
                                   'Введите Ваш любимый цвет',
                                   parse_mode="Markdown",
                                   reply_markup=types.ReplyKeyboardRemove())
            bot.register_next_step_handler(msg, color_step)
        elif message.text == book_btn:
            msg = bot.send_message(chat_id,
                                   'Введите название Вашей любимой книги',
                                   parse_mode="Markdown",
                                   reply_markup=types.ReplyKeyboardRemove())
            bot.register_next_step_handler(msg, book_step)
        elif message.text == continue_btn:
            msg = bot.send_message(chat_id,
                                   message_for_more_info,
                                   parse_mode="Markdown",
                                   reply_markup=markup_for_transitions_with_next)
            bot.register_next_step_handler(msg, more_info_step)
        elif message.text == back_btn:
            msg = bot.send_message(chat_id,
                                   'Выберите размер сюрприз бокса',
                                   parse_mode="Markdown",
                                   reply_markup=markup_for_sizes)
            bot.register_next_step_handler(msg, choise_form)
        elif message.text == menu_btn:
            send_menu(message)
        elif message.text == return_btn:
            user = user_dict[chat_id]
            user.rele = True
            msg = bot.send_message(chat_id,
                                   getRegData(user, 'Ваша анкета, ', message.from_user.first_name),
                                   parse_mode="Markdown",
                                   reply_markup=markup_for_transitions_with_pay)
            bot.register_next_step_handler(msg, pay_step)
        else:
            user = user_dict[chat_id]
            if user.rele:
                markup1 = markup_for_choise_form_after_final
            else:
                markup1 = markup_for_choise_form
            msg = bot.send_message(chat_id,
                                   'Ошибка. Воспользуйтесь кнопками для выбора раздела или для перехода между этапами',
                                   parse_mode="Markdown",
                                   reply_markup=markup1)
            bot.register_next_step_handler(msg, choise_rele)
    except Exception as e:
        bot.reply_to(message, message_for_except, reply_markup=markup_with_menu)


def autor_step(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        if user.rele:
            markup = markup_for_choise_form_after_final
        else:
            markup = markup_for_choise_form
        if message.content_type == 'text':
            user.autor = message.text
            msg = bot.send_message(chat_id,
                                   'Автор добавлен в анкету',
                                   parse_mode="Markdown",
                                   reply_markup=markup)
            bot.register_next_step_handler(msg, choise_rele)
        else:
            msg = bot.send_message(chat_id,
                                   'Пожалуйста, введите автора с клавиатуры',
                                   parse_mode="Markdown",
                                   reply_markup=types.ReplyKeyboardRemove())
            bot.register_next_step_handler(msg, autor_step)
    except Exception as e:
        bot.reply_to(message, message_for_except, reply_markup=markup_with_menu)


def film_step(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        if user.rele:
            markup = markup_for_choise_form_after_final
        else:
            markup = markup_for_choise_form
        if message.content_type == 'text':
            user.film = message.text
            msg = bot.send_message(chat_id,
                                   'Фильм добавлен в анкету',
                                   parse_mode="Markdown",
                                   reply_markup=markup)
            bot.register_next_step_handler(msg, choise_rele)
        else:
            msg = bot.send_message(chat_id,
                                   'Пожалуйста, введите фильм с клавиатуры',
                                   parse_mode="Markdown",
                                   reply_markup=types.ReplyKeyboardRemove())
            bot.register_next_step_handler(msg, film_step)
    except Exception as e:
        bot.reply_to(message, message_for_except, reply_markup=markup_with_menu)


def serial_step(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        if user.rele:
            markup = markup_for_choise_form_after_final
        else:
            markup = markup_for_choise_form
        if message.content_type == 'text':
            user.serial = message.text
            msg = bot.send_message(chat_id, 'Сериал добавлен в анкету',
                                   parse_mode="Markdown",
                                   reply_markup=markup)
            bot.register_next_step_handler(msg, choise_rele)
        else:
            msg = bot.send_message(chat_id,
                                   'Пожалуйста, введите сериал с клавиатуры',
                                   parse_mode="Markdown",
                                   reply_markup=types.ReplyKeyboardRemove())
            bot.register_next_step_handler(msg, serial_step)
    except Exception as e:
        bot.reply_to(message, message_for_except, reply_markup=markup_with_menu)


def painter_step(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        if user.rele:
            markup = markup_for_choise_form_after_final
        else:
            markup = markup_for_choise_form
        if message.content_type == 'text':
            user.painter = message.text
            msg = bot.send_message(chat_id,
                                   'Художник добавлен в анкету',
                                   parse_mode="Markdown",
                                   reply_markup=markup)
            bot.register_next_step_handler(msg, choise_rele)
        else:
            msg = bot.send_message(chat_id,
                                   'Пожалуйста, введите художника с клавиатуры',
                                   parse_mode="Markdown",
                                   reply_markup=types.ReplyKeyboardRemove())
            bot.register_next_step_handler(msg, painter_step)
    except Exception as e:
        bot.reply_to(message, message_for_except, reply_markup=markup_with_menu)


def poet_step(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        if user.rele:
            markup = markup_for_choise_form_after_final
        else:
            markup = markup_for_choise_form
        if message.content_type == 'text':
            user.poet = message.text
            msg = bot.send_message(chat_id,
                                   'Поэт добавлен в анкету',
                                   parse_mode="Markdown",
                                   reply_markup=markup)
            bot.register_next_step_handler(msg, choise_rele)
        else:
            msg = bot.send_message(chat_id,
                                   'Пожалуйста, введите поэта с клавиатуры',
                                   parse_mode="Markdown",
                                   reply_markup=types.ReplyKeyboardRemove())
            bot.register_next_step_handler(msg, poet_step)
    except Exception as e:
        bot.reply_to(message, message_for_except, reply_markup=markup_with_menu)


def music_group_step(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        if user.rele:
            markup = markup_for_choise_form_after_final
        else:
            markup = markup_for_choise_form
        if message.content_type == 'text':
            user.music_group = message.text
            msg = bot.send_message(chat_id,
                                   'Музыкальная группа добавлена в анкету',
                                   parse_mode="Markdown",
                                   reply_markup=markup)
            bot.register_next_step_handler(msg, choise_rele)
        else:
            msg = bot.send_message(chat_id, 'Пожалуйста, музыкальную группу с клавиатуры', parse_mode="Markdown",
                                   reply_markup=types.ReplyKeyboardRemove())
            bot.register_next_step_handler(msg, music_group_step)
    except Exception as e:
        bot.reply_to(message, message_for_except, reply_markup=markup_with_menu)


def game_step(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        if user.rele:
            markup = markup_for_choise_form_after_final
        else:
            markup = markup_for_choise_form
        if message.content_type == 'text':
            user.game = message.text
            msg = bot.send_message(chat_id,
                                   'Игра добавлен в анкету',
                                   parse_mode="Markdown",
                                   reply_markup=markup)
            bot.register_next_step_handler(msg, choise_rele)
        else:
            msg = bot.send_message(chat_id,
                                   'Пожалуйста, введите компьютерную игру с клавиатуры',
                                   parse_mode="Markdown",
                                   reply_markup=types.ReplyKeyboardRemove())
            bot.register_next_step_handler(msg, game_step)
    except Exception as e:
        bot.reply_to(message, message_for_except, reply_markup=markup_with_menu)


def color_step(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        if user.rele:
            markup = markup_for_choise_form_after_final
        else:
            markup = markup_for_choise_form
        if message.content_type == 'text':
            user.color = message.text
            msg = bot.send_message(chat_id,
                                   'Любимый цвет добавлен в анкету',
                                   parse_mode="Markdown",
                                   reply_markup=markup)
            bot.register_next_step_handler(msg, choise_rele)
        else:
            msg = bot.send_message(chat_id,
                                   'Пожалуйста, введите цвет с клавиатуры',
                                   parse_mode="Markdown",
                                   reply_markup=types.ReplyKeyboardRemove())
            bot.register_next_step_handler(msg, color_step)
    except Exception as e:
        bot.reply_to(message, message_for_except, reply_markup=markup_with_menu)


def book_step(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        if user.rele:
            markup = markup_for_choise_form_after_final
        else:
            markup = markup_for_choise_form
        if message.content_type == 'text':
            user.book = message.text
            msg = bot.send_message(chat_id,
                                   'Любимая книга добавлена в анкету',
                                   parse_mode="Markdown",
                                   reply_markup=markup)
            bot.register_next_step_handler(msg, choise_rele)
        else:
            msg = bot.send_message(chat_id,
                                   'Пожалуйста, введите книгу с клавиатуры',
                                   parse_mode="Markdown",
                                   reply_markup=types.ReplyKeyboardRemove())
            bot.register_next_step_handler(msg, book_step)
    except Exception as e:
        bot.reply_to(message, message_for_except, reply_markup=markup_with_menu)


def more_info_step(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        if message.content_type == 'text':
            if message.text == back_btn:
                if user.rele:
                    markup = markup_for_choise_form_after_final
                else:
                    markup = markup_for_choise_form
                msg = bot.send_message(chat_id,
                                       'Выберите раздел',
                                       parse_mode="Markdown",
                                       reply_markup=markup)
                bot.register_next_step_handler(msg, choise_rele)
            elif message.text == continue_btn:
                msg = bot.send_message(chat_id,
                                       'Введите ФИО',
                                       parse_mode="Markdown",
                                       reply_markup=markup_for_transitions_with_next)
                bot.register_next_step_handler(msg, FIO_step)
            elif message.text == menu_btn:
                send_menu(message)
            else:
                user.more_info = message.text
                msg = bot.send_message(chat_id,
                                       'Введите ФИО',
                                       parse_mode="Markdown",
                                       reply_markup=markup_for_transitions_with_next)
                bot.register_next_step_handler(msg, FIO_step)
        else:
            msg = bot.send_message(chat_id,
                                   'Пожалуйста, введите дополнительную информацию с клавиатуры',
                                   parse_mode="Markdown",
                                   reply_markup=markup_for_transitions_with_next)
            bot.register_next_step_handler(msg, more_info_step)
    except Exception as e:
        bot.reply_to(message, message_for_except, reply_markup=markup_with_menu)


def FIO_step(message):
    try:
        chat_id = message.chat.id
        if message.content_type == 'text':
            if message.text == back_btn:
                msg = bot.send_message(chat_id,
                                       message_for_more_info,
                                       parse_mode="Markdown",
                                       reply_markup=markup_for_transitions_with_next)
                bot.register_next_step_handler(msg, more_info_step)
            elif message.text == continue_btn:
                msg = bot.send_message(chat_id,
                                       'В какой стране Вы проживаете?',
                                       parse_mode="Markdown",
                                       reply_markup=markup_for_county)
                bot.register_next_step_handler(msg, country_step)
            elif message.text == menu_btn:
                send_menu(message)
            else:
                chat_id = message.chat.id
                user = user_dict[chat_id]
                user.FIO = message.text
                msg = bot.send_message(chat_id,
                                       'В какой стране Вы проживаете?',
                                       parse_mode="Markdown",
                                       reply_markup=markup_for_county)
                bot.register_next_step_handler(msg, country_step)
        else:
            msg = bot.send_message(chat_id,
                                   'Пожалуйста, введите ФИО с клавиатуры',
                                   parse_mode="Markdown",
                                   reply_markup=markup_for_transitions_with_next)
            bot.register_next_step_handler(msg, FIO_step)
    except Exception as e:
        bot.reply_to(message, message_for_except, reply_markup=markup_with_menu)


def country_step(message):
    try:
        chat_id = message.chat.id
        if message.content_type == 'text':
            if message.text == back_btn:
                msg = bot.send_message(chat_id,
                                       'Введите ФИО',
                                       parse_mode="Markdown",
                                       reply_markup=markup_for_transitions_with_next)
                bot.register_next_step_handler(msg, FIO_step)
            elif message.text == continue_btn:
                msg = bot.send_message(chat_id,
                                       'Введите индекс',
                                       parse_mode="Markdown",
                                       reply_markup=markup_for_transitions_with_next)
                bot.register_next_step_handler(msg, index_step)
            elif message.text == menu_btn:
                send_menu(message)
            elif message.text == other_country_btn:
                msg = bot.send_message(chat_id,
                                       'Введите название страны',
                                       parse_mode="Markdown",
                                       reply_markup=markup_for_transitions_with_next)
                bot.register_next_step_handler(msg, print_country_step)
            elif message.text == russia_btn:
                user = user_dict[chat_id]
                user.country = message.text
                msg = bot.send_message(chat_id,
                                       'Введите индекс',
                                       parse_mode="Markdown",
                                       reply_markup=markup_for_transitions_with_next)
                bot.register_next_step_handler(msg, index_step)
            else:
                user = user_dict[chat_id]
                user.country = message.text
                msg = bot.send_message(chat_id,
                                       'Введите индекс',
                                       parse_mode="Markdown",
                                       reply_markup=markup_for_transitions_with_next)
                bot.register_next_step_handler(msg, index_step)
        else:
            msg = bot.send_message(chat_id,
                                   'Пожалуйста, введите страну с клавиатуры или воспользуйтесь кнопками',
                                   parse_mode="Markdown",
                                   reply_markup=markup_for_transitions_with_next)
            bot.register_next_step_handler(msg, country_step)
    except Exception as e:
        bot.reply_to(message, message_for_except, reply_markup=markup_with_menu)


def print_country_step(message):
    try:
        chat_id = message.chat.id
        if message.content_type == 'text':
            if message.text == back_btn:
                msg = bot.send_message(chat_id,
                                       'В какой стране Вы проживаете?',
                                       parse_mode="Markdown",
                                       reply_markup=markup_for_county)
                bot.register_next_step_handler(msg, country_step)
            elif message.text == continue_btn:
                msg = bot.send_message(chat_id,
                                       'Введите индекс',
                                       parse_mode="Markdown",
                                       reply_markup=markup_for_transitions_with_next)
                bot.register_next_step_handler(msg, index_step)
            elif message.text == menu_btn:
                send_menu(message)
            else:
                user = user_dict[chat_id]
                user.index = message.text
                msg = bot.send_message(chat_id,
                                       'Введите индекс',
                                       parse_mode="Markdown",
                                       reply_markup=markup_for_transitions_with_next)
                bot.register_next_step_handler(msg, index_step)
        else:
            msg = bot.send_message(chat_id,
                                   'Пожалуйста, введите страну с клавиатуры или воспользуйтесь кнопками',
                                   parse_mode="Markdown",
                                   reply_markup=markup_for_transitions_with_next)
            bot.register_next_step_handler(msg, print_country_step)
    except Exception as e:
        bot.reply_to(message, message_for_except, reply_markup=markup_with_menu)


def index_step(message):
    try:
        chat_id = message.chat.id
        if message.content_type == 'text':
            if message.text == back_btn:
                msg = bot.send_message(chat_id,
                                       'В какой стране Вы проживаете?',
                                       parse_mode="Markdown",
                                       reply_markup=markup_for_county)
                bot.register_next_step_handler(msg, country_step)
            elif message.text == continue_btn:
                msg = bot.send_message(chat_id,
                                       'Введите город',
                                       parse_mode="Markdown",
                                       reply_markup=markup_for_transitions_with_next)
                bot.register_next_step_handler(msg, city_step)
            elif message.text == menu_btn:
                send_menu(message)
            else:
                chat_id = message.chat.id
                user = user_dict[chat_id]
                user.index = message.text
                msg = bot.send_message(chat_id,
                                       'Введите город',
                                       parse_mode="Markdown",
                                       reply_markup=markup_for_transitions_with_next)
                bot.register_next_step_handler(msg, city_step)
        else:
            msg = bot.send_message(chat_id,
                                   'Пожалуйста, введите индекс с клавиатуры',
                                   parse_mode="Markdown",
                                   reply_markup=markup_for_transitions_with_next)
            bot.register_next_step_handler(msg, index_step)
    except Exception as e:
        bot.reply_to(message, message_for_except, reply_markup=markup_with_menu)


def city_step(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        if message.content_type == 'text':
            if message.text == back_btn:
                msg = bot.send_message(chat_id,
                                       'Введите индекс',
                                       parse_mode="Markdown",
                                       reply_markup=markup_for_transitions_with_next)
                bot.register_next_step_handler(msg, index_step)
            elif message.text == continue_btn:
                user.rele = False
                msg = bot.send_message(chat_id,
                                       'Введите адрес',
                                       parse_mode="Markdown",
                                       reply_markup=markup_for_transitions_with_next)
                bot.register_next_step_handler(msg, adres_step)
            elif message.text == menu_btn:
                send_menu(message)
            else:
                user.city = message.text
                user.rele = False
                msg = bot.send_message(chat_id,
                                       'Введите адрес',
                                       parse_mode="Markdown",
                                       reply_markup=markup_for_transitions_with_next)
                bot.register_next_step_handler(msg, adres_step)
        else:
            msg = bot.send_message(chat_id,
                                   'Пожалуйста, введите город с клавиатуры',
                                   parse_mode="Markdown",
                                   reply_markup=markup_for_transitions_with_next)
            bot.register_next_step_handler(msg, city_step)
    except Exception as e:
        bot.reply_to(message, message_for_except, reply_markup=markup_with_menu)


def adres_step(message):
    try:
        chat_id = message.chat.id
        if message.content_type == 'text':
            if message.text == back_btn:
                msg = bot.send_message(chat_id,
                                       'Введите город',
                                       parse_mode="Markdown",
                                       reply_markup=markup_for_transitions_with_next)
                bot.register_next_step_handler(msg, city_step)
            elif message.text == continue_btn:
                user = user_dict[chat_id]
                user.rele = True
                msg = bot.send_message(chat_id,
                                       getRegData(user, 'Ваша анкета, ', message.from_user.first_name),
                                       parse_mode="Markdown",
                                       reply_markup=markup_for_transitions_with_pay)
                bot.register_next_step_handler(msg, pay_step)
            elif message.text == menu_btn:
                send_menu(message)
            else:
                user = user_dict[chat_id]
                user.adres = message.text
                user.rele = True
                msg = bot.send_message(chat_id,
                                       getRegData(user, 'Ваша анкета, ', message.from_user.first_name),
                                       parse_mode="Markdown",
                                       reply_markup=markup_for_transitions_with_pay)
                bot.register_next_step_handler(msg, pay_step)
        else:
            msg = bot.send_message(chat_id,
                                   'Пожалуйста, введите адрес с клавиатуры',
                                   parse_mode="Markdown",
                                   reply_markup=markup_for_transitions_with_next)
            bot.register_next_step_handler(msg, adres_step)
    except Exception as e:
        bot.reply_to(message, message_for_except, reply_markup=markup_with_menu)


def pay_step(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        if message.text == pay_btn:
            if user.country == russia_btn or user.country == 'Россия' or user.country == 'Russia' or \
                    user.country == 'russia' or user.country == 'россия':
                if user.size == big_size_btn:
                    bot.send_message(chat_id,
                                     'Заказ большого бокса по России - 4900 рублей',
                                     parse_mode="Markdown")
                elif user.size == medium_size_btn:
                    bot.send_message(chat_id,
                                     'Заказ среднего бокса по России - 3900 рублей',
                                     parse_mode="Markdown")
                elif user.size == small_size_btn:
                    bot.send_message(chat_id,
                                     'Заказ маленького бокса по России - 2900 рублей',
                                     parse_mode="Markdown")
            else:
                if user.size == big_size_btn:
                    bot.send_message(chat_id,
                                     'Заказ большого бокса по миру - 6500 рублей',
                                     parse_mode="Markdown")
                elif user.size == medium_size_btn:
                    bot.send_message(chat_id,
                                     'Заказ среднего бокса по миру - 5500 рублей',
                                     parse_mode="Markdown")
                elif user.size == small_size_btn:
                    bot.send_message(chat_id,
                                     'Заказ маленького бокса по миру - 4500 рублей',
                                     parse_mode="Markdown")
            msg = bot.send_message(chat_id,
                                   'Пожалуйста, приложите скриншот или документ оплаты,\n'
                                   'чтобы мы могли приступить к выполнению заказа\n'
                                   'Номер карты: 4276600042956215\n'
                                   'ФИО: Тинатин Георгиевна',
                                   reply_markup=markup_with_back)
            bot.register_next_step_handler(msg, ready_step)

        elif message.text == back_btn:
            msg = bot.send_message(chat_id,
                                   'Введите адрес',
                                   parse_mode="Markdown",
                                   reply_markup=markup_for_transitions_with_next)
            bot.register_next_step_handler(msg, adres_step)
            user.rele = False
        elif message.text == edit_form_btn:
            msg = bot.send_message(chat_id,
                                   'Выберите раздел и дайте нам знать, что Вам нравится больше всего',
                                   parse_mode="Markdown",
                                   reply_markup=markup_for_choise_form_after_final)
            bot.register_next_step_handler(msg, choise_rele)
        elif message.text == edit_size_btn:
            msg = bot.send_message(chat_id,
                                   'Выберите размер сюрприз бокса',
                                   parse_mode="Markdown",
                                   reply_markup=markup_for_sizes_after_final)
            bot.register_next_step_handler(msg, edit_size)
        elif message.text == menu_btn:
            send_menu(message)
        else:
            msg = bot.send_message(chat_id,
                                   'Ошибка!!! Воспользуйтесь кнопками для совершения оплаты или возврата назад',
                                   parse_mode="Markdown",
                                   reply_markup=markup_for_transitions_with_pay)
            bot.register_next_step_handler(msg, pay_step)
    except Exception as e:
        bot.reply_to(message, message_for_except, reply_markup=markup_with_menu)


def edit_size(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        text = message.text
        if text == big_size_btn or text == medium_size_btn or text == small_size_btn:
            user.size = text
            user.rele = True
            msg = bot.send_message(chat_id,
                                   getRegData(user, 'Ваша анкета, ', message.from_user.first_name),
                                   parse_mode="Markdown",
                                   reply_markup=markup_for_transitions_with_pay)
            bot.register_next_step_handler(msg, pay_step)
        elif text == return_btn:
            user.rele = True
            msg = bot.send_message(chat_id,
                                   getRegData(user, 'Ваша анкета, ', message.from_user.first_name),
                                   parse_mode="Markdown",
                                   reply_markup=markup_for_transitions_with_pay)
            bot.register_next_step_handler(msg, pay_step)
        else:
            msg = bot.send_message(chat_id,
                                   'Ошибка. Воспользуйтесь кнопками для выбора размера',
                                   parse_mode="Markdown",
                                   reply_markup=markup_for_sizes_after_final)
            bot.register_next_step_handler(msg, edit_size)
    except Exception as e:
        bot.reply_to(message, message_for_except, reply_markup=markup_with_menu)


def ready_step(message):
    chat_id = message.chat.id
    to_chat_id = TG_ANKETS_CHANNEL_ID
    user = user_dict[chat_id]
    if message.content_type == 'photo' or message.content_type == 'document':
        if user.country == russia_btn or user.country == 'Россия' or user.country == 'Russia' or \
                user.country == 'russia' or user.country == 'россия':
            if user.size == big_size_btn:
                bot.send_message(to_chat_id,
                                 'Заказ большого бокса по России - 4900 рублей',
                                 parse_mode="Markdown")
            elif user.size == medium_size_btn:
                bot.send_message(to_chat_id,
                                 'Заказ среднего бокса по России - 3900 рублей',
                                 parse_mode="Markdown")
            elif user.size == small_size_btn:
                bot.send_message(to_chat_id,
                                 'Заказ маленького бокса по России - 2900 рублей',
                                 parse_mode="Markdown")
        else:
            if user.size == big_size_btn:
                bot.send_message(to_chat_id,
                                 'Заказ большого бокса по миру - 6500 рублей',
                                 parse_mode="Markdown")
            elif user.size == medium_size_btn:
                bot.send_message(to_chat_id,
                                 'Заказ среднего бокса по миру - 5500 рублей',
                                 parse_mode="Markdown")
            elif user.size == small_size_btn:
                bot.send_message(to_chat_id,
                                 'Заказ маленького бокса по миру - 4500 рублей',
                                 parse_mode="Markdown")
        if message.from_user.username is None:
            bot.send_message(to_chat_id,
                             getRegData(user, 'Анкета пользователя ', message.from_user.first_name),
                             parse_mode="Markdown")
            bot.send_message(chat_id,
                               message_for_notice,
                               reply_markup=keyboard_for_end)
            msg = bot.send_message(message.chat.id,
                                   'Для возврата нажмите "В меню"',
                                   reply_markup=markup_with_menu)
        else:
            bot.send_message(to_chat_id,
                             getRegData(user, 'Анкета пользователя @', message.from_user.username),
                             parse_mode="Markdown")
            bot.send_message(chat_id,
                                   thanks_for_the_order,
                                   reply_markup=keyboard_for_end)
            msg = bot.send_message(message.chat.id,
                                   'Для возврата нажмите "В меню"',
                                   reply_markup=markup_with_menu)

        bot.forward_message(to_chat_id, chat_id, message.id)
        bot.register_next_step_handler(msg, menu)
    elif message.text == back_btn:
        user = user_dict[chat_id]
        user.rele = True
        msg = bot.send_message(chat_id,
                               getRegData(user, 'Ваша анкета, ', message.from_user.first_name),
                               parse_mode="Markdown",
                               reply_markup=markup_for_transitions_with_pay)
        bot.register_next_step_handler(msg, pay_step)
    else:
        msg = bot.send_message(chat_id,
                               'Необходимо приложить скриншот или документ с оплатой\n'
                               'чтобы мы могли приступить к выполнению заказа\n'
                               'Номер карты: 4276600042956215\n'
                               'ФИО: Тинатин Георгиевна',
                               reply_markup=markup_with_back)
        bot.register_next_step_handler(msg, ready_step)


def menu(message):
    try:
        send_menu(message)
    except Exception as e:
        bot.reply_to(message, message_for_except, reply_markup=markup_with_menu)


@bot.message_handler(content_types=["text", "audio", "document", "photo", "sticker", "video", "video_note", "voice",
                                    "location", "contact", "new_chat_members", "left_chat_member", "new_chat_title",
                                    "new_chat_photo", "delete_chat_photo", "group_chat_created",
                                    "supergroup_chat_created", "channel_chat_created", "migrate_to_chat_id",
                                    "migrate_from_chat_id", "pinned_message"])
def send_welcome(message):
    try:
        send_menu(message)
    except Exception as e:
        bot.reply_to(message, message_for_except, reply_markup=markup_with_menu)


if __name__ == '__main__':
    bot.polling(none_stop=True)