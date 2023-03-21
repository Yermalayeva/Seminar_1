import input8
import output
import editor

while True:

    choise = int(input('Введите нужное действие: \n 1-добавить справочник \
               \n 2-Вывести всех \n 3-Поиск по фамилии \n 4-Редактировать контакт \n 5-Удалить контакт \n 6-Выход \n'))
    match choise:
        case 1:
            input8.input(input('Введите имя: '), input('Введите номер: '))
        case 2:
            output.OutputAll()
        case 3:
            output.Search(input('Введите фамилию: '))
        case 4: 
            editor.Edit(input('Введите фамилию или номер контакта для изменений: '))
        case 5:
            editor.Delete(input('Введите фамилию и номер контакта для удаления: '))
        case 6: break



        
