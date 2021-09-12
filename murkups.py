from telebot.types import ReplyKeyboardMarkup

menu_btn = '⚠️В меню⚠️'
back_btn = '👈🏼Назад'
continue_btn = 'Далее👉🏼'
autor_btn = 'Автор'
film_btn = 'ФИЛЬМ'
serial_btn = 'Сериал'
painter_btn = 'Художник'
poet_btn = 'Поэт'
music_btn = 'Музыка'
game_btn = 'Игра'
color_btn = 'Цвет'
book_btn = 'Книга'
small_size_btn = '🎁Маленький📕'
medium_size_btn = '🎁🎁Средний📕📕'
big_size_btn = '🎁🎁🎁Большой📕📕📕'
return_btn = '👈🏼Вернуться в анкету'
russia_btn = '🇷🇺Россия🇷🇺'
other_country_btn = 'Другая страна❓'
edit_form_btn = '🤔Редактировать анкету🤔'
edit_size_btn = '🎁Редактировать размер бокса🎁'
pay_btn = '🎉Оплатить🎉'
form_command = '/form 🎁'
about_command = '/about ℹ'
comment_command = '/comment 👀'
links_command = '/links 📞'
faq_command = '/faq ❓'

markup_for_commands = ReplyKeyboardMarkup(resize_keyboard=True)
markup_for_commands.row(form_command)
markup_for_commands.row(about_command, links_command)
markup_for_commands.row(comment_command, faq_command)

markup_with_menu = ReplyKeyboardMarkup(resize_keyboard=True)
markup_with_menu.row(menu_btn)

markup_for_choise_form = ReplyKeyboardMarkup(resize_keyboard=True)
markup_for_choise_form.row(autor_btn, film_btn, serial_btn)
markup_for_choise_form.row(painter_btn, poet_btn, music_btn)
markup_for_choise_form.row(game_btn, color_btn, book_btn)
markup_for_choise_form.row(back_btn, menu_btn, continue_btn)

markup_for_sizes = ReplyKeyboardMarkup(resize_keyboard=True)
markup_for_sizes.row(small_size_btn)
markup_for_sizes.row(medium_size_btn)
markup_for_sizes.row(big_size_btn)

markup_for_sizes_after_final = ReplyKeyboardMarkup(resize_keyboard=True)
markup_for_sizes_after_final.row(small_size_btn)
markup_for_sizes_after_final.row(medium_size_btn)
markup_for_sizes_after_final.row(big_size_btn)
markup_for_sizes_after_final.row(return_btn)

markup_for_county = ReplyKeyboardMarkup(resize_keyboard=True)
markup_for_county.row(russia_btn, other_country_btn)
markup_for_county.row(back_btn, menu_btn, continue_btn)

markup_with_back = ReplyKeyboardMarkup(resize_keyboard=True)
markup_with_back.row(back_btn)

markup_for_transitions_with_next = ReplyKeyboardMarkup(resize_keyboard=True)
markup_for_transitions_with_next.row(back_btn, menu_btn, continue_btn)

markup_for_transitions_with_pay = ReplyKeyboardMarkup(resize_keyboard=True)
markup_for_transitions_with_pay.row(edit_form_btn)
markup_for_transitions_with_pay.row(edit_size_btn)
markup_for_transitions_with_pay.row(back_btn, menu_btn, pay_btn)

markup_for_choise_form_after_final = ReplyKeyboardMarkup(resize_keyboard=True)
markup_for_choise_form_after_final.row(autor_btn, film_btn, serial_btn)
markup_for_choise_form_after_final.row(painter_btn, poet_btn, music_btn)
markup_for_choise_form_after_final.row(game_btn, color_btn, book_btn)
markup_for_choise_form_after_final.row(return_btn, menu_btn, continue_btn)