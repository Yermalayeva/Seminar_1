#Требуется найти N-е число Фибоначчи
#a0 = 0, a1 = 1, a[k] = a[k-1] + a[k-2] (k > 1).

#Задача №31: Последовательностью Фибоначчи называетпоследовательность чисел a0,
# a1, ..., an, ..., где a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
#Input: 7
#Output: 21
#Задание необходимо решать через рекурсию
"""
def GetUserNumber(message_to_user):
    flag = True
    while flag:
        try:
            print(message_to_user)
            n = int(input())
            if n or n == 0:
                flag = False
                return n
        except ValueError:
            print('Ошибка ввода! Введено не число')

def Fibonaci(num):
    if num == 1 or num == 2:
        return num     
    else:         
        return Fibonaci(num-1)+Fibonaci(num-2)    
    
a = GetUserNumber('Введите число: ') 
print(Fibonaci(a))
"""

#########################################

#Задача №33:Хакер Василий получил доступ к классному журналу и хочет заменить
# все свои минимальные оценки на максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все максимальные – на минимальные.
#Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1
"""
array = [int(i) for i in input().split()]
def ChangeMaxtoMin(array):
    min = max = array[0]
    #max = array[0]
    
    for i in array:
        if i > max:
            max = i
        if i < min:
            min = i
    for i in range(len(array)):
        if array[i] == max:
            array[i]= min
    return array
    

print(ChangeMaxtoMin(array))
"""

###########################################

# Задача №35: Напишите функцию, которая принимает одно число и проверяет,
#  является ли оно простым. Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)
#Input: 5
#Output: yes

"""
num = int(input('Введите число: ')) 

def IsSimple(num):
    

    for i in range(2,num):         
        if num%i == 0:             
            print('Число не простое')             
            break     
    else: 
        if num <= 1:
            print('Число не простое и не составное')  
        else:      
            print('Число простое') 
IsSimple(num)
"""


###############################################

#Задача №37: Дано натуральное число N и последовательность из N элементов.
#Требуется вывести эту последовательность в обратном порядке.
#Примечание. В программе запрещается объявлять массивы и использовать циклы(даже для ввода и вывода).
#Input: 2 -> 3 4
#Output: 4 3
"""
num = int(input('Введите число элементов: '))
def Reverse(num):
    if num==0:
        return
    el = int(input('Введите число: '))
    Reverse(num-1)
    print(el)
Reverse(num)
"""

# Импорт фунции. Вариант 1
#import modul1

#print(modul1.max1(5,9))

#Вариант 2:

#from modul1 import max1

#print(max1(5,9))

#Пользователь вводит число N и необходимо вывести N первых чисел
#  последовательности Фибоначчи

"""
def fib(n):
    if n in [1,2]:
        return 1
    return fib(n - 1) + fib(n - 2)

list_1 = []

for i in range(1,10):
    list_1.append(fib(i))
print(list_1)
"""

#Задача: Два друга решили поиграть в игру. Один загадывает число, другой отгадывает.
#Быстрая сортировка

"""
def quick_sort(array):
    if len(array) <= 1:
        return array
    else:
        pivor = array[0]
    less = [i for i in array[1:]if i <= pivor]
    qreater = [i for i in array[1:]if i > pivor]
    return quick_sort(less) + [pivor] + quick_sort(qreater)

print(quick_sort([10,5,2]))
"""


