class User:
    def __init__(self, size=None, autor='✍🏻', film='🎬', serial='🎦', painter='🎨', poet='📜',
                 music_group='🥁', game='🎮', color='🌈', book='📕', more_info='ℹ️',
                 FIO='Это необходимо было указать для осуществления доставки',
                 country='Это необходимо было указать для осуществления доставки',
                 city='Это необходимо было указать для осуществления доставки',
                 index='Это необходимо было указать для осуществления доставки',
                 adres='Это необходимо было указать для осуществления доставки',
                 rele=False):
        self.size = size
        self.autor = autor
        self.film = film
        self.serial = serial
        self.painter = painter
        self.poet = poet
        self.music_group = music_group
        self.game = game
        self.color = color
        self.book = book
        self.more_info = more_info
        self.FIO = FIO
        self.country = country
        self.city = city
        self.index = index
        self.adres = adres
        self.rele = rele