def OutputAll():

    with open('file.txt', 'r', encoding='utf-8') as file:
        for line in file:
            print(line)


def Search(data):
    with open('file.txt', 'r', encoding='utf-8') as file:
        flag = False
        for line in file:

            if data in line.lover():
                print(line)
                flag = True
        if flag == False:
            print('\n не найдено \n')
