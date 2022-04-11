class Date:

    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def method_class(cls, date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        date11 = cls(day, month, year)
        print(cls, date_as_string)
        return date11

    @staticmethod
    def method_static(date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        if day <= 31 and day != 0 and month <= 12 and month != 0 and year <= 4999:
            print(date_as_string)
            return day, month, year
        else:
            print('Ошибка ввода данных')


d = '11-04-2022'
date1 = Date.method_class(d)
date2 = Date.method_static(d)
print(date1)
print(date2)