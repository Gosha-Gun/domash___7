class Number(ValueError):
    pass


my_list = []
while True:
    try:
        value = input('Введите число в список:')
        if value == 'stop':
            break
        if not value.isdigit():
            raise Number(value)
        my_list.append(int(value))
    except Number as ex:
        print('Вы ввели не число!', ex)
print(my_list)
