from itertools import count
from random import randint
import time
print('Программа подбрасывания монетки - Орел-Решка')
eagle = 'Орёл'
flag = 'Решка'
action = input('Введите 1, если хотите подбросить монету, или q - чтобы выйти из программы')
while action == 'q':
    if action == 1:
        time.sleep(3)
        number = randint(1, 2)
        if number == 1:
            print(f'Выпал {eagle}')
        else:
            print(f'Выпала {flag}')
    action = input('Введите 1, если хотите подбросить монету, или q - чтобы выйти из программы')
print('Вы вышли из программы')