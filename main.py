from random import *

# Функция проверки числа (является ли введенные данные числом и входит ли это число в диапазон от 1 до 100
def is_valid(number):
    if number.isdigit() and 1 <= int(number) <= 100:
        return True
    if input('Вы ввели некоректное число. Хотели бы повторить? Введите да/нет ').lower() in ['да', 'lf']:
        start()
    return False

# Функция приветствия
def hello():
    print('Добро пожаловать в "4исл0вую угадайку"\n'
          'Правила игры просты:\n'
          'Я загадал число от 1 до 100\n'
          'Тебе нужно угадать это число\n')
    input('Понятно? Для продолжения нажми Enter')

# Функция ввода числа
def start():
    print()
    x = input('Введите число от 1 до 100\n')
    if is_valid(x):
        game(x)

# Функция алгоритма игры
def game(x):
    if int(x) == random_digit:
        print('Угадал')
    else:
        print('Не угадал, давай еще')
        start()


random_digit = randint(1, 100)
hello()
start()