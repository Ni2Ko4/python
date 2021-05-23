num_1 = int(input('Введи положительное число'))
num_2 = int(input('Введи целое отрицательное число'))

def my_func(x, y):
    a = x
    # x = x ** y
    # Другой вариант решения
    while y != -1:
        x = x * a
        y += 1
    x = 1 / x
    print(x)

if num_1 > 0 and num_2 < 0:
    my_func(num_1, num_2)
else:
    print('Внимательно прочитай условия ввода и попробуй ещё раз')

