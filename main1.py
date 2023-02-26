# Задача9

#n = int(input())
#factorial = 1
#while n>0:
#   factorial*=n
#   n -= 1

#print(f'Факториал числа {n} равен {factorial}')

#################################################

# Задача11

# n = int(input())
# prev_num=0
# current_num=1
# temp=None
# count=0
# while prev_num<=n:
#     count+=1
#     if n==prev_num:
#         print(count)
#         break
#     temp=prev_num
#    prev_num=current_num+prev_num
#    current_num=temp
#
# else:
#    print(f'Число не является числом Фибоначчи ')


##################################################

# Задача13

# N = 3
# count = 0
# max_days=0
# while N > 0:
#     day_temperature=int(input('Введите температуру:'))
#     if day_temperature > 0:
#         count += 1
#     else:
#        count = 0

#     if max_days < count:
#        max_days = count
#        N -= 1

# print(f'Максимальное количество дней оттепели: {max_days}')


#############################################################

#Задача15

# n - число арбузов

# Найти минимум и максимум веса

#n = int(input())

#max = 0
#min = 10000000
#for i in range(n):
#    ves_arbyz = int(input())
#    if ves_arbyz < min:
#        min = ves_arbyz
#    if ves_arbyz > max:
#        max = ves_arbyz

#print (max, min)

