class Drees:
    def __init__(self, size, growth):
        self.size = size
        self.growth = growth

    def get_square_coat(self):
        return self.size / 6.5 + 0.5

    def get_square_costume(self):
        return self.growth * 2 + 0.3

    @property
    def get_sq_full(self):
        return str(f'Oбщая площадь ткани \n'
                   f' {(self.size / 6.5 + 0.5) + (self.growth * 2 + 0.3)}')


class Coat(Drees):
    def __init__(self, size, growth):
        super().__init__(size, growth)
        self.square_coat = round(self.size / 6.5 + 0.5)

    def __str__(self):
        return f'Площадь на пальто {self.square_coat}'


class Costume(Drees):
    def __init__(self, size, height):
        super().__init__(size, height)
        self.square_costume = round(self.growth * 2 + 0.3)

    def __str__(self):
        return f'Площадь на костюм {self.square_costume}'

coat = Coat(4, 7)
Costume = Costume(2, 5)
print(coat)
print(Costume)
print(coat.get_square_coat())
print(Costume.get_square_costume())
print(coat.get_sq_full)
print(Costume.get_sq_full)