# Задача 12: Петя и Катя – брат и сестра.
# Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
# Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.



x = int(input())
y = int(input())
c = 0
for i in range(x + y):
    if c:
        break
    for j in range(x + y):
        if i + j == x and i * j == y:
            c = 1
            print(*sorted([i, j]))
            break