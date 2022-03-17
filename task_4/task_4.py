import os

directory = r'.'
groups = [100, 1000, 10000, 100000]
result = dict.fromkeys(groups, 0)

for path_from_top, subdirs, files in os.walk(directory):
    for file in files:
        path = os.path.join(path_from_top, file)
        size = os.path.getsize(path)
        to_group = min(filter(lambda x: size < x, groups))
        result[to_group] += 1

b100 = result[100]
b1000 = result[1000]
b10000 = result[10000]
b100000 = result[100000]
print(f" {result} \n Тут {b100} файлов размером не более 100 байт;\n {b1000} файла больше 100 и не больше 1000;\n {b10000} файла больше 1000 и не больше 10000;\n И {b100000} файла больше 10000 и не больше 100000;")