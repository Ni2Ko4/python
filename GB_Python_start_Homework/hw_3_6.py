def my_funk(word):
    latin = 'qwertyuiopasdfghjklzxcvbnm'
    return word.title() if not set(word).difference(latin) else False

words = input('Введите строку из слов разделённых пробелами').split()
for w in words:
    result = my_funk(w)
    if result:
        print(my_funk(w), ' ')