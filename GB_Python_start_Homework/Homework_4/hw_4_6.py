from itertools import count, cycle

print('Для генерации числа нажми Enter, либо q для выхода')
for i in count(int(input('Введи число'))):
    print(i, end='')
    quit = input()
    if quit == 'q':
        break

print('Для генерации числа нажми Enter, либо q для выхода')
u_list = input('Введите список, разделяя элементы пробелом: ').split()
iter_ = cycle(u_list)
quit = None

while quit != 'q':
    print(next(iter_), end='')
    quit = input()
