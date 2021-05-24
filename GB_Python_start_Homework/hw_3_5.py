def sum():
    b = 0
    while True:
        numbers = input('Введи число или Q для выхода').split()
        for num in numbers:
            if num == 'q':
                return b
            else:
                try:
                    b += int(num)
                except ValueError:
                    print('Нажми Q для выхода')
        print(f'Сумма чисел = {b}')
print(sum())