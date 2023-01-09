import csv
import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, updater, ConversationHandler

#  Запускаем логгирование
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)

logger = logging.getLogger(__name__)

TOKEN = '5848862768:AAEF2p4rJVvewH0I5TTi8Mv815GXg0UJ6c8'



def run():
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('all', open_file))
    dispatcher.add_handler(CommandHandler('help', help_info))

    add_user_handler = ConversationHandler(
        entry_points=[CommandHandler('add', add_values)],
        states={
            1: [MessageHandler(Filters.text & ~Filters.command, set_first_name)],
            2: [MessageHandler(Filters.text & ~Filters.command, set_last_name)],
            3: [MessageHandler(Filters.text & ~Filters.command, set_phone)],
            4: [MessageHandler(Filters.text & ~Filters.command, set_description)],
        },
        fallbacks=[CommandHandler('stop', stop_operation)]
    )
    dispatcher.add_handler(add_user_handler)

    del_user_handler = ConversationHandler(
        entry_points=[CommandHandler('del', del_user)],
        states={
            1: [MessageHandler(Filters.text & ~Filters.command, del_user_set_id)],
        },
        fallbacks=[CommandHandler('stop', stop_operation)]
    )
    dispatcher.add_handler(del_user_handler)

    search_user_handler = ConversationHandler(
        entry_points=[CommandHandler('search', search_user)],
        states={
            1: [MessageHandler(Filters.text & ~Filters.command, search_user_set_filter)],
        },
        fallbacks=[CommandHandler('stop', stop_operation)]
    )
    dispatcher.add_handler(search_user_handler)

    updater.start_polling()
    updater.idle()


def start(update, context):
    context.bot.send_message(update.effective_chat.id, "Привет! Добро пожаловать в телефонный справочник.")


def all_users(update, context):
    users = phonebook_model.get_all_users()
    if len(users) == 0:
        context.bot.send_message(update.effective_chat.id, "Список пуст")
        return

    result = users_to_str(users)
    context.bot.send_message(update.effective_chat.id, result)


def help_info(update, context):
    result = "/all - выводит все контакты\n"
    result += "/add - добавляет новый контакт\n"
    result += "/del - удаляет контакт по id\n"
    result += "/search - ищет контакт по фамилии\n"
    result += "/stop - отменяет начатую операцию"
    context.bot.send_message(update.effective_chat.id, result)


def users_to_str(users: [{}]):
    result = ""
    for u in users:
        result += f'{u["id"]}. {u["first_name"]} {u["last_name"]}: {u["phone"]} ({u["description"]})\n'
    return result


# Вывод открытого справочника
def printer(book_list):
    global values
    values = book_list
    return values


def step(step_next):
    printer(open_file())
    for i in values:
        print(i)
    if step_next == 1:
        printer(open_file())
        step(show_menu())
    elif step_next == 2:
        search_name(values)
        step(show_menu())
    elif step_next == 3:
        find_values_by_room(values)
        step(show_menu())
    elif step_next == 4:
        add_values(values)
        step(show_menu())
    elif step_next == 5:
        dell_values(values)
        step(show_menu())
    elif step_next == 6:
        update_values(values)
        step(show_menu())
    elif step_next == 7:
        save_values(values)
        step(show_menu())

def add_values(book):
    temp = {}
    temp["id"] = int(input('Введите ID нового ученика: '))
    temp["last_name"] = input('Введите фамилию нового ученика: ')
    temp["first_name"] = input('Введите имя нового ученика: ')
    temp["room"] = input('Введите класс нового ученика: ')
    temp["phone_number"] = input('Введите телефон нового ученика: ')
    book.append(temp)
    for item in book:
        print(item)
    return book



def dell_values(book):
    id_user = int(input("Введите ID для удаления: "))
    for index, student in enumerate(book):
        if id_user == student['id']:
            del book[index]
    for item in book:
        print(item)
    return book



def open_file():
    student = []
    with open('database.csv', 'r', encoding='utf-8') as fin:
        csv_reader = csv.reader(fin)
        for row in csv_reader:
            temp = {}
            temp["id"] = int(row[0])
            temp["last_name"] = row[1]
            temp["first_name"] = row[2]
            temp["room"] = row[3]
            temp["phone_number"] = row[4]
            student.append(temp)
    return student

def save_values(book_list):
    with open('database.csv', 'w+', encoding='utf-8') as save_employyee_book:
        csv_writer = csv.writer(save_employyee_book, lineterminator='\r')
        for student in book_list:
            csv_writer.writerow(student.values())


def search_name(values):
    print("\n" + "=" * 20)
    print("Выберите необходимое действие")
    print("1. Найти ученика по ID")
    print("2. Найти ученика по Фамилии")
    print("3. Найти ученика по Имени")
    print("4. Найти ученика по классу")

    step = int(input("Введите номер необходимого действия: "))

    if step == 1:
        id_user = int(input("Введите ID ученика: "))
        for student in values:
            if id_user == student['id']:
                print(student)

    elif step == 2:
        last_name = input("Введите фамилию ученика: ")
        for student in values:
            if last_name in student['last_name']:
                print(student)
    elif step == 3:
        first_name = input("Введите имя ученика: ")
        for student in values:
            if first_name in student['first_name']:
                print(student)
    elif step == 4:
        room = input("Введите имя ученика: ")
        for student in values:
            if room in student['room']:
                print(student)
    else:
        print("Не корректный ввод.")




def find_values_by_room(students: list) -> list:
    result = []
    pos = input('Введите класс: ')
    for student in students:
        if pos in student["room"]:
            result.append(student)
    for item in result:
        print(item)




def update_values(book):
    user_iput_id = int(input('Введите ID ученика для изменения данных: '))
    for temp in book:
        if temp["id"] == user_iput_id:
            print("\n" + "=" * 20)
            print("Выберите необходимое действие")
            print('1. Изменить фамилию')
            print('2. Изменить имя')
            print('3. Изменить класс')
            print('4. Изменить телефон')
            step = int(input("Введите номер необходимого действия: "))
            if step == 1:
                temp["last_name"] = input('Введите фамилию нового ученика: ')
            elif step == 2:
                temp["first_name"] = input('Введите имя нового ученика: ')
            elif step == 3:
                temp["room"] = input('Введите класс нового ученика: ')
            elif step == 4:
                temp["phone_number"] = input('Введите телефон нового ученика: ')
    for i in book:
        print(i)
    return book


def show_menu() -> int:
    print("Выбрать действия")
    print("1. Загрузить список учеников")
    print("2. Найти ученика")
    print("3. Выбрать учеников по классу")
    print("4. Добавить")
    print("5. Удалить")
    print("6. Обновить")
    return int(input("Введите команду: "))











def execute():
    step(show_menu())



execute()











