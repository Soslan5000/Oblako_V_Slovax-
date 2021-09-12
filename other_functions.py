from string import Template

def getRegData(user, title, name):
    t = Template(
        '$title*$name*'
        ' \nФИО: *$FIO* \nСтрана: *$country*'
        '\nГород: *$city* \nАдрес: *$adres*'
        '\nИндекс: *$index* \nРазмер бокса: *$size*'
        '\nЛюбимый автор: *$autor* \nЛюбимый фильм: *$film*'
        '\nЛюбимый сериал: *$serial* \nЛюбимый художник: *$painter*'
        '\nЛюбимый поэт: *$poet* \nЛюбимая музыкальная группа: *$music_group*'
        '\nЛюбимая игра: *$game* \nЛюбимый цвет: *$color*'
        '\nЛюбимая книга: *$book* \nДополнительная информация: *$more_info*')

    return t.substitute({
        'title': title,
        'name': name,
        'FIO': user.FIO,
        'country': user.country,
        'city': user.city,
        'adres': user.adres,
        'index': user.index,
        'size': user.size,
        'autor': user.autor,
        'film': user.film,
        'serial': user.serial,
        'painter': user.painter,
        'poet': user.poet,
        'music_group': user.music_group,
        'game': user.game,
        'color': user.color,
        'book': user.book,
        'more_info': user.more_info,
    })