# Создать телефонный справочник с возможностью импорта и экспорта
# данных в формате .txt. Фамилия, Имя, Отчество, номер телефона -
# данные, которые находятся в файле.

# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска 
# определенной записи (фамилии человека)

# 4. Использование функций. Ваша программа не должна быть линейной

# 1)Добавить
# 2)Ввести всех
# 3)Поиск по фамилии



def input(data, number):

    with open('file.txt', 'a', encoding='utf-8') as file:
        file.write(f'{data} : {number}\n')
    print('Добавлено')
    