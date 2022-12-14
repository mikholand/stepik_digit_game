from random import *
from sys import exit

count = 0

# Функция проверки начала диапазона (является ли введенные данные числом)
def range_begin():
    x = input('Введите начало диапазона: ')
    if x.isdigit():
        return int(x)
    print('Вы ввели некоректное число.')
    request()

# Функция проверки конца диапазона (является ли введенные данные числом)
def range_end():
    y = input('Введите конец диапазона: ')
    if y.isdigit():
        return int(y)
    print('Вы ввели некоректное число.')
    request()

# Функция проверки корректности числа
def is_valid(number, x, y):
    if str(number).isdigit() and x <= int(number) <= y:
        return True
    print(f'Вы ввели некоректное число. Необходимо было ввести число от {x} до {y}.')
    request()

# Функция приветствия
def hello():
    print('Добро пожаловать в "Угадай число" v.2.0\n'
          'Правила игры просты:\n'
          'Я буду загадывать число, а вы отгадывать\n'
          'Диапазон чисел задаете сами\n'
          'Например, от 1 до 10 или от 128 до 256')
    input('Для дальнейшей инструкции нажми Enter')

# Функция диапазона игры
def range_game():
    x = range_begin()
    y = range_end()
    if x == y:
        print('Вы ввели одинаковое начало и конец. Такой диапазон недопустим.')
        request()
    elif x > y:
        x, y = y, x
    return x, y

# Функция запуска игры
def start():
    print()
    x, y = range_game()
    print(f'Я загадал число от {x} до {y}. Теперь можешь попробовать угадать его.')
    random_digit = randint(x, y)
    game(random_digit, x, y)

# Функция перезапуска игры
def restart():
    global count
    count = 0
    request()

# Функция для запроса на повтор ввода новых чисел
def request():
    answer = input('Хотели бы повторить? Введите да/нет ')
    if answer.lower() in ['да', 'lf']:
        start()
    elif answer.lower() in ['нет', 'ytn']:
        print('Очень жаль и спасибо за игру!')
        exit()
    else:
        print('Я вас не понимаю! Ответьте на вопрос.')
        request()

# Функция вывода количества попыток
def print_count(count):
    if count == 1:
        print('Вау! А вы везунчик! Отгадали его с 1 попытки')
    elif count == 2:
        print('Весьма неплохо! Отгадали его со 2 попытки')
    elif count >= 3:
        print(f'Отгадали его с {count} попытки')

# Функция алгоритма игры
def game(random_digit, x, y):
    global count
    digit = input(f'Введите число от {x} до {y}: ')
    count += 1
    if is_valid(digit, x, y):
        digit = int(digit)
        if digit == random_digit:
            print('Вы угадали число! Поздравляю!')
            print_count(count)
            restart()
        elif digit < random_digit:
            print('Ваше число оказалось меньше загаданного. Попробуй еще раз.')
            game(random_digit, x, y)
        elif digit > random_digit:
            print('Ваше число оказалось больше загаданного. Попробуй еще раз.')
            game(random_digit, x, y)


hello()
start()