from random import *

# Функция проверки начала диапазона (является ли введенные данные числом)
def range_begin():
    x = input('Введите начало диапазона: ')
    if x.isdigit():
        return int(x)
    if input('Вы ввели некоректное число. Хотели бы повторить? Введите да/нет ').lower() in ['да', 'lf']:
        start()
    return False

def range_end():
    y = input('Введите конец диапазона: ')
    if y.isdigit():
        return int(y)
    if input('Вы ввели некоректное число. Хотели начать заново? Введите да/нет ').lower() in ['да', 'lf']:
        start()
    return False

def is_valid(number, x, y):
    if str(number).isdigit() and x <= int(number) <= y:
        return True
    if input(f'Вы ввели некоректное число. Необходимо ввести число от {x} до {y}.'
             'Хотели бы повторить? Введите да/нет ').lower() in ['да', 'lf']:
        start()
    return False

# Функция приветствия
def hello():
    print('Добро пожаловать в "Угадай число" v.2.0\n'
          'Правила игры просты:\n'
          'Я буду загадывать число, а вы отгадывать\n'
          'Диапазон чисел задаете сами\n'
          'Например, от 1 до 10 или от 128 до 256')
    input('Для дальнейшей инструкции нажми Enter')

# Функция
def range_game():
    x = range_begin()
    y = range_end()
    if x == y:
        print('Вы ввели одинаковое начало и конец. Такой диапазон недопустим.')
        if input('Хотели начать заново? Введите да/нет ').lower() in ['да', 'lf']:
            start()
    elif x > y:
        x, y = y, x
    return x, y


# Функция ввода числа
def start():
    print()
    x, y = range_game()
    print(f'Я загадал число от {x} до {y}. Теперь можешь попробовать угадать его.')
    random_digit = randint(x, y)
    game(random_digit, x, y)

def restart():
    if input('Хотели начать заново? Введите да/нет ').lower() in ['да', 'lf']:
        start()
    else:
        print('Спасибо за игру!')


# Функция алгоритма игры
def game(random_digit, x, y):
    digit = input(f'Введите число от {x} до {y}: ')
    if is_valid(digit, x, y):
        digit = int(digit)
        if digit == random_digit:
            print('Вы угадали число! Поздравляю!')
            restart()
        elif digit < random_digit:
            print('Ваше число оказалось меньше загаданного. Попробуй еще раз.')
            game(random_digit, x, y)
        elif digit > random_digit:
            print('Ваше число оказалось больше загаданного. Попробуй еще раз.')
            game(random_digit, x, y)


hello()
start()