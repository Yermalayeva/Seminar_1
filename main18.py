#Задача 18: Требуется найти в массиве A[1..N] самый близкий
# по величине элемент к заданному числу X. Пользователь в первой
# строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. 
#Последняя строка содержит число X

#*Пример:*
# 5          # N-количество элементов в массиве
# 1 2 3 4 5  # массив
# 6          # Заданное число
# -> 5       # Самый близкий элемент к заданному числу

n = int(input('Введите количество элементов массива: '))
list = [i for i in range(1, n + 1)]
print(list)

x = int(input('Ввести заданное число: '))
element = list[0]
for i in range(1, len(list)):
    if(abs (list[i]-x)< abs(element-x)) or abs(list[i]-x) == abs(element-x) and list[i]< element:
        element = list[i]

print(element)
