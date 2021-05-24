from functools import reduce
list_main = range(100, 1001, 2)

def comp (num_1, num_2,):
    return num_1 * num_2

print(reduce(comp, list_main))