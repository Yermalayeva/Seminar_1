# Задача 1) Вводится список целых чисел в одну строчку через пробел.
# Необходимо оставить в нем только двузначные числа.
#Реализовать программу с использованием функции filter.
# Результат отобразить на экране в виде последовательности
#оставшихся чисел в одну строчку через пробел.
#[1,2,3,4,22,234,24] ----> [22, 24]
"""
list1 = [int(x) for x in input().split()]
res = list(filter(lambda x: x>9 and x<100, list1))
print(res)
"""

#Задача 2) Напишите программу, которая принимает на вход вещественное
#  число и показывает сумму его цифр.

#Пример:
#- 6782 -> 23
#- 0,56 -> 11
"""
num = input('Введите число: ')
res = list(filter(lambda x: x != '-' and x != ',' and x != '.', num))
res = sum(list(map(lambda x: int(x), res)))
print(res)
"""
"""
#2 вариант
print(sum(map(int, filter(lambda el: el.isdigit(), input('Enter a number: ')))))
"""


#Задача 3)
#[12,'sadf',5643] ---> ['sadf'] ,[12,5643]

"""
list1 =[x for x in input().split()]
res1 = list(filter(lambda el: el.isdigit(), list1))
res2 = list(filter(lambda el: el.isdigit()== False, list1))

print (res1, res2)
"""




