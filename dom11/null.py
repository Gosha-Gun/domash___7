class exception:
    def __init__(self, dividend, divider):
        self.dividend = dividend
        self.divider = divider

    @staticmethod
    def divide_null(dividend, divider):
        try:
            return (dividend / divider)
        except:
            return (f"Деление на ноль недопустимо")


div = exception(10, 100)
print(exception.divide_null(111, 3))
print(exception.divide_null(100, 0.2))
print(div.divide_null(100, 0))