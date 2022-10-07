import random, math
min_num = input('Введите минимальное число: ')
while not min_num.isdigit():
    min_num = input('Введите минимальное число: ')
min_num = int(min_num)
max_num = input('Введите максимальное число: ')
while not max_num.isdigit():
    max_num = input('Введите максимальное число: ')
max_num = int(max_num)
secret_number = random.randint(min_num, max_num)
tries = math.log(max_num - min_num)
tries = math.ceil(tries)
print(f'Компьютер загадал число от {min_num} до {max_num}. Твоя задача - угадать число за {tries} попыток.')
while tries > 0:
    number = input('Ваше число: ')
    if not number.isdigit():
        print('Вы ввели не число')
        continue
    number = int(number)
    if number == secret_number:
        print(f'Вы угадали! Это число - {secret_number}')
        break
    elif number < secret_number:
        print('Ваше число меньше загаданного')
    elif number > secret_number:
        print('Ваше число больше загаданного')
    tries-=1
    print(f'Осталось {tries} попыток')