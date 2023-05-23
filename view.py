def display_menu():
    print('Выберите действие для телефонного справочника\n'
          '1 - Найти контакт по фамилии\n'
          '2 - Добавить контакт\n'
          '3 - Удалить контакт\n'
          '4 - Изменить контакт\n'
          '5 - Посмотреть все контакты\n'
          '6 - Выход\n')


def display_contact(name, phone_number):
    if phone_number is None:
        print(f"Контакт {name} не найден")
    else:
        print(f"Фамилия {name}, номер телефона {phone_number}")


def display_message(message):
    print(message)


def display_contacts(contacts):
    if not contacts:
        print("Телефонная книга пуста")

    else:
        for contact in contacts:
            print(
                f"Фамилия {contact.name}, номер телефона {contact.phone_number}")
