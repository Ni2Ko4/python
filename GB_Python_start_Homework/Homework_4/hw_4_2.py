list_orig = [4, 5, 77, 39, 20, 8, 43, 93, 4, 5, 92]
print([list_orig[num] for num in range(1, len(list_orig)) if list_orig[num] > list_orig[num - 1]])
