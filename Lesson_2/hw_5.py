my_list = [3, 2, 5 ,6, 3, 6, 7, 1]
num = int(input('Введите число от 1 до 9'))
if num in my_list:
    my_list.reverse()
    a = len(my_list) - my_list.index(num)
    my_list.reverse()
    my_list.insert(a, num)
    print(my_list)
else:
    my_list.append(num)
    print(my_list)