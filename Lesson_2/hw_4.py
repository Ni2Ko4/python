my_str = input('Введите слова через пробел')
my_str = my_str.split(' ')
for a, b in enumerate(my_str, 1):
    print(a, b)


#number = 0
#number_2 = 1
#while number_2 <= len(my_str):
#    print(number_2, my_str[number])
#    number = number + 1
#    number_2 = number_2 + 1