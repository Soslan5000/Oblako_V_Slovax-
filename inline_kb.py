from telebot.types import InlineKeyboardMarkup
from telebot.types import InlineKeyboardButton

keyboard_for_links = InlineKeyboardMarkup()
btn = InlineKeyboardButton(text='Отзывы', url='https://vk.com/topic-205226603_48064476')
btn1 = InlineKeyboardButton(text='ВК создателя oblako_v_slovax', url='https://vk.com/engry_nps')
btn2 = InlineKeyboardButton(text='Tik-tok создателя oblako_v_slovax:', url='https://www.tiktok.com/@oblako_v_slovax?lang=ru-RU')
btn3 = InlineKeyboardButton(text='Телега создателя oblako_v_slovax', url='https://t.me/Engry_nps')
btn4 = InlineKeyboardButton(text='Наша группа ВК', url='https://vk.com/oblako_v_slovax')
btn5 = InlineKeyboardButton(text='ВК создателя бота', url='https://vk.com/electroenergetik')
btn6 = InlineKeyboardButton(text='Телега создателя бота', url='https://t.me/GoogBye')
keyboard_for_links.row(btn)
keyboard_for_links.row(btn1)
keyboard_for_links.row(btn2)
keyboard_for_links.row(btn3)
keyboard_for_links.row(btn4)
keyboard_for_links.row(btn5)
keyboard_for_links.row(btn6)

keyboard_for_comment = InlineKeyboardMarkup()
btn = InlineKeyboardButton(text='Отзывы', url='https://vk.com/topic-205226603_48064476')
keyboard_for_comment.add(btn)

keyboard_for_faq = InlineKeyboardMarkup()
btn = InlineKeyboardButton(text='FAQ', url='https://t.me/oblako_v_slovax_FAQ')
keyboard_for_faq.add(btn)

keyboard_for_end = InlineKeyboardMarkup()
btn = InlineKeyboardButton(text='Отзывы', url='https://vk.com/topic-205226603_48064476')
btn1 = InlineKeyboardButton(text='Телега оператора', url='https://t.me/Engry_nps')
keyboard_for_end.add(btn)
keyboard_for_end.add(btn1)
