list_1 = input('Введите значения через пробел')
list_1 = list_1.split(' ')
print(list_1)
lenth = len(list_1)
a = 0
b = 1
if lenth % 2 == 0:
    while b < lenth:
        list_1[a], list_1[b] = list_1[b], list_1[a]
        a = a + 2
        b = b + 2
else:
    while a + 1 != lenth:
        list_1[a], list_1[b] = list_1[b], list_1[a]
        a = a + 2
        b = b + 2
print(list_1)
