path = "phonebook.txt"

def create_file():
    data = open(path, 'a', encoding='UTF-8')
    data.close()

def adding_info_file():
    data = open(path, 'a', encoding='UTF-8')
    first_name = input("Введите имя: ").capitalize()
    mid_name = input("Введите отчество: ").capitalize()
    last_name = input("Введите фамилию: ").capitalize()
    phone = input("Введите номер телефона: ")
    data.write(f"{first_name} {mid_name} {last_name}: {phone}\n")
    data.close()

def reading_file():
    with open(path, 'r', encoding="UTF-8") as data:
        contacts = data.read()
        print(f"Список контактов:\n{contacts}\n")

def finding_contact_file():
    finding_name = input("Поиск: ")
    matching_lines = []
    with open(path, 'r', encoding="UTF-8") as data:
        for line in data:
            contact_info = line.rstrip().split()
            if any(contact == finding_name for contact in contact_info):
                matching_lines.append(line)
    if matching_lines:
        if len(matching_lines) > 1:
            print("Найдено несколько контактов.")
            for i, matching_line in enumerate(matching_lines, start=1):
                print(f"{i}. {matching_line.rstrip()}")
            choice = int(input("Выберите нужный контакт: "))
            if 1 <= choice <= len(matching_lines):
                print(matching_lines[choice - 1].rstrip())
                return matching_lines[choice - 1].rstrip()
            else:
                print("Некорректный номер контакта")
        else:
            print(matching_lines[0].rstrip())
            return matching_lines[0].rstrip()
    else:
        print("Контакт не найден")
        return None

def change_contact():
    show_info = input("Показать телефонную книгу?: \n1. Да\n2. Нет\n")
    if show_info == "1":
        reading_file()
    contact = finding_contact_file()
    if contact is not None:
        what_change = input("Что требуется изменить?\n1. Имя\n2. Отчество\n3. Фамилия\n4. Номер телефона\n5. Контакт полностью:\n")
        if what_change == '5':
            first_name = input("Введите новое имя: ").capitalize()
            mid_name = input("Введите новое отчество: ").capitalize()
            last_name = input("Введите новую фамилию: ").capitalize()
            phone = input("Введите новый номер телефона: ")
        else:
            new_data = input("Введите новые данные для контакта: ")

        with open(path, 'r+', encoding="UTF-8") as file:
            lines = file.readlines()
            file.seek(0)
            for line in lines:
                contact_info = line.rstrip().split(":")
                name_parts = contact_info[0].split()
                phone = contact_info[1].strip()
                if line.rstrip().startswith(contact):
                    if what_change == '1':
                        name_parts[0] = new_data.capitalize()
                    elif what_change == '2':
                        name_parts[1] = new_data.capitalize()
                    elif what_change == '3':
                        name_parts[2] = new_data.capitalize()
                    elif what_change == '4':
                        phone = new_data
                    elif what_change == '5':
                        name_parts = [first_name.capitalize(), mid_name.capitalize(), last_name.capitalize()]
                        phone = phone
                    updated_contact = " ".join(name_parts) + ": " + phone + "\n"
                    file.write(updated_contact)
                    contact = updated_contact.rstrip()
                else:
                    file.write(line)
            file.truncate()

        print("Контакт успешно изменен.")
        print(contact)




def delete_contact():
    show_info = input("Показать телефонную книгу?: \n1. Да\n2. Нет\n")
    if show_info == "1":
        reading_file()
    contact = finding_contact_file()
    if contact is not None:
        delete_agree = input("Удалить выбраный контакт?\n1. Да\n2. Отмена\n")
        if delete_agree == '1':
            with open(path, 'r+', encoding="UTF-8") as file:
                lines = file.readlines()
                file.seek(0)
                for line in lines:
                    if line.rstrip().startswith(contact):
                        deleted_contact = ""
                        file.write(deleted_contact)
                        contact = deleted_contact.rstrip()
                    else:
                        file.write(line)
                file.truncate()

        print("Контакт успешно удален.")
        reading_file()


def menu():
    while True:
        selected_action = input("Выберите действие:\n1. Показать телефонную книгу\n2. Добавить контакт\n3. Найти контакт\n4. Изменить контакт\n5. Удалить контакт\n6. Выход\n")
        
        if selected_action == "1":
            reading_file()
            menu_return = input("Выберите действие:\n1. Вернуться в меню\n2. Выход\n")
            if menu_return == "1":
                continue
            else:
                return
        elif selected_action == "2":
            adding_info_file()
            menu_return = input("Выберите действие:\n1. Вернуться в меню\n2. Выход\n")
            if menu_return == "1":
                continue
            else:
                return
        elif selected_action == "3":
            finding_contact_file()
            menu_return = input("Выберите действие:\n1. Вернуться в меню\n2. Выход\n")
            if menu_return == "1":
                continue
            else:
                return
        elif selected_action == "4":
            change_contact()
            menu_return = input("Выберите действие:\n1. Вернуться в меню\n2. Выход\n")
            if menu_return == "1":
                continue
            else:
                return
        elif selected_action == "5":
            delete_contact()
            menu_return = input("Выберите действие:\n1. Вернуться в меню\n2. Выход\n")
            if menu_return == "1":
                continue
            else:
                return


create_file()
menu()