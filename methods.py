import json


def save(phonebook):
    with open("phoneNumber.json", "w", encoding="utf-8") as doc:
        doc.write(json.dumps(phonebook, ensure_ascii=False))
    print("Все изменения сохранены.")


def load():
    with open("phoneNumber.json", "r", encoding="utf-8") as doc:
        phonebook = json.load(doc)
    print("Данные загружены на локальное хранилище.")
    return phonebook


def exit(phonebook):
    save(phonebook)
    print("Завершение работы")


def print_all(phonebook):
    print("Текущий телефонный список")
    for name in phonebook:
        print(name, end=" ")
        for key in phonebook[name]:
            print(f"{key}: {phonebook[name][key]}", end=" ")
        print()


def print_help():
    print("Список команд: \n"
          "/save - сохраняет изменения, \n"
          "/load - загружает данные на локальное хранилище, \n"
          "/exit - закончить работу со справочником, \n"
          "/all - просмотреть текущий справочник, \n"
          "/add - добавить данные в справочник, \n"
          "/delete - удалить запись из справочника, \n"
          "/search - поиск по имени, \n"
          "/update - изменить данные, \n")


def add(phonebook):
    name = input("Введите имя: ")
    phone = input("Введите номера телефонов через пробел: ").split()
    if phone:
        phonebook[name] = {'phones': phone}
    birthday = input("Введите дату рождения: ")
    if birthday:
        phonebook[name].update({"birthday": birthday})
    email = input("Введите адрес электронной почты: ")
    if email:
        phonebook[name].update({"email": email})


def delete(phonebook):
    name = input("Введите имя контакта: ")
    try:
        del phonebook[name]
        print(f"Контакт {name} был удален")
    except:
        print("Такого контакта нет в справочнике.")


def search(phonebook):
    name = input("Введите имя: ")
    print(phonebook[name])


def update(phonebook):
    name = input("Введите имя: ")
    print("Что вы хотите изменить (1 - имя, 2 - телефон, 3 - дата рождения, 4 - эмаил)?")
    while True:
        new_command = input()
        if new_command == "1":
            new_name = input("Введите новое имя: ")
            phonebook[new_name] = phonebook[name]
            del phonebook[name]
            name = new_name
        elif new_command == "2":
            phone = input('Введите новые номера телефона через пробел: ').split()
            phonebook[name].update({'phones': phone})
        elif new_command == "3":
            birthday = input("Введите новую дату рождения: ")
            phonebook[name].update({'birthday': birthday})
        elif new_command == "4":
            email = input("Введите новый email: ")
            phonebook[name].update({'email': email})
        else:
            print("Такой команды нет.")
        if input("Хотите изменить еще что-нибудь? Y/N ").lower() != "y":
            break
