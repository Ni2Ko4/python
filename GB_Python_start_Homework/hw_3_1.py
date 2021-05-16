num_1 = float(input('Введи первое число'))
num_2 = float(input('Введи второе число'))
if num_2 != 0:
    print(round((lambda x, y: x / y)(num_1, num_2), 3))
else:
    print('Ты, что! На 0 делить нельзя!')