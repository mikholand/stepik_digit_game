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
    print('Добро пожаловать в "Угадай число"\n'
          'Правила игры просты:\n'
          'Я загадал число от 1 до 100\n'
          'Вам нужно угадать это число\n')
    input('Для продолжения нажми Enter')

# Функция ввода числа
def start():
    print()
    x = input('Введите число от 1 до 100\n')
    if is_valid(x):
        game(x)

# Функция алгоритма игры
def game(x):
    x = int(x)
    if x == random_digit:
        print('Вы угадали число! Поздравляю!')
    elif x < random_digit:
        print('Ваше число оказалось меньше загаданного. Попробуй еще раз.')
        start()
    elif x > random_digit:
        print('Ваше число оказалось больше загаданного. Попробуй еще раз.')
        start()


random_digit = randint(1, 100)
hello()
start()