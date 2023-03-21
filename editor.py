def Delete(data):
    data = data.lower()
    data_file = []
    with open('file.txt', 'r', encoding='utf-8') as file:
        for line in file:
            if data not in line.lower():
                data_file.append(line)
    str_data_file = ' '.join(data_file)
    with open('file.txt', 'w', encoding='utf-8') as file:
        file.write(str_data_file)
        print('удалено')

def Edit(data):
    data = data.lower()
    data_file = []
    with open('file.txt', 'r', encoding='utf-8') as file:
        for line in file:
            if data not in line.lower():
                data_file.append(line)
            else:
                temp = line.split(':')
                if data in temp[0].lower():
                    temp[0] = input('введите новую фамилию и имя: ')
                elif data in temp[1].lower():
                    temp[1] = input('введите новый номер телефона: ')
                data_file.append(f'{temp[0]} : {temp[1]}')

    str_data_file = ' '.join(data_file)  
    with open('file.txt', 'w', encoding='utf-8') as file:
        file.write(str_data_file)
        print('редактировано')
