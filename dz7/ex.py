import csv


def import_values(data, sep=None):
    with open('phone.csv', 'a+') as file:
        if sep == None:
            for i in data:
                file.write(f"{i}\n")
            file.write(f"\n")
        else:
            file.write(sep.join(data))
            file.write(f"\n")




def export_values():
    with open('phone.csv', 'r') as file:
        data = []
        t = []
        for line in file:
            if ',' in line:
                temp = line.strip().split(',')
                data.append(temp)
            elif ';' in line:
                temp = line.strip().split(';')
                data.append(temp)
            elif ':' in line:
                temp = line.strip().split(':')
                data.append(temp)
            elif '-' in line:
                temp = line.strip().split('-')
                data.append(temp)
            elif line != '':
                if line != '\n':
                    t.append(line.strip())
                else:
                    data.append(t)
                    t= []
    return data


def input_values():
    last_name = input("Введите фамилию: ")
    first_name = input("Введите имя: ")
    phone_number = input("Введите телефон: ")
    note = input("Введите примечание: ")
    return [last_name, first_name, phone_number, note]

def set_separator():
    sep = input("Введите разделитель: ")
    if sep == "":
        sep = None
    return sep

def execute():
    print("Что желаем сделать:\n\
    1 - импорт;\n\
    2 - экспорт;\n\
    3 - поиск контакта.")
    ch = input("Введите цифру: ")
    if ch == '1':
        sep = set_separator()
        import_values(input_values(), sep)
    elif ch == '2':
        data = export_values()
        print_values(data)
    else:
        word = input("Введите данные для поиска: ")
        data = export_values()
        item = search_values(word, data)
        if item != None:
            print("Фамилия".center(20), "Имя".center(20), "Телефон".center(15), "Примечание".center(30))
            print("-"*85)
            print(item[0].center(20), item[1].center(20), item[2].center(15), item[3].center(30))
        else:
            print("Данные не обнаружены")


def print_values(data):
    if len(data) > 0:
        print("Фамилия".center(20), "Имя".center(20), "Телефон".center(15), "Примечание".center(30))
        print("-"*85)
        for item in data:
            print(item[0].center(20), item[1].center(20), item[2].center(15), item[3].center(30))
    else:
        print("Справочник пуст!")


def search_values(word, data):
    if len(data) > 0:
        for item in data:
            if word in item:
                return item
    else:
        return None



execute()


