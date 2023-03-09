#Задача 32: Определить индексы элементов массива (списка), значения 
#которых принадлежат заданному диапазону (т.е. не меньше заданного 
#минимума и не больше заданного максимума)


from random import randint
array = []
for i in range(0,10):
    array.append(randint(1,20))
print(array)

min = int(input('Введите минимальное значение: '))
max = int(input('Введите максимальное значение: '))
for i in range(len(array)):
    if min <= array[i] <= max:
        array.append(i)
        print(i)



