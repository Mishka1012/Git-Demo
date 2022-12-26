# Student
# sample solution
# 12/26/2022

# функция для получения строки из заданной строки,
# в которой все вхождения первого символа заменены на '$',
# кроме самого первого символа.
def change_char(string):
    # извлекаем первый символ
    first = string[0]
    # меняем символы в строке на доллары
    string = string.replace(first, "$")
    # соеденяем и возвращаем строку
    return first + string[1:]

# переписать функцию change_char так, чтобы она использовала геренатор
def change_char(string):
    # извлекаем первый символ
    first = string[0]
    # реализуем генератор
    return "".join([first] + [char if char != first else "$" for char in string[1:]])