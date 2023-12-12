from methods import *

try:
    phonebook = load()
except:
    phonebook = {"Ваня": {"phones": [123, 445],
                          "birthday": "01.12.1999",
                          "email": "tbg.ru"},
                 "Дядя Вася": {"phones": [1234, 678]}
                 }

while True:
    command = input("Введите команду ")
    if command == "/exit":
        exit(phonebook)
        break
    elif command == "/all":
        print_all(phonebook)
    elif command == "/save":
        save(phonebook)
    elif command == "/load":
        phonebook = load()
    elif command == "/help":
        print_help()
    elif command == "/add":
        add(phonebook)
    elif command == "/delete":
        delete(phonebook)
    elif command == "/search":
        search(phonebook)
    elif command == "/update":
        update(phonebook)
    else:
        print("Неопознанная команда, просьба изучить мануал через /help")
    print()