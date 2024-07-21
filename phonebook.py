def work_with_phonebook():
    choice = show_menu()
    phone_book = read_txt('phonebook.txt')

    while choice != 7:
        if choice == 1:
            print_result(phone_book)
        elif choice == 2:
            last_name = input('Введите фамилию: ')
            print(find_by_lastname(phone_book, last_name))
        elif choice == 3:
            number = input('Введите номер телефона: ')
            print(find_by_number(phone_book, number))
        elif choice == 4:
            user_data = input('Введите данные нового абонента (Фамилия Имя Отчество Номер): ')
            add_user(phone_book, user_data)
            write_txt('phonebook.txt', phone_book)
        elif choice == 5:
            write_txt('phonebook.txt', phone_book)
            print("Данные сохранены в файл.")
        elif choice == 6:
            copy_line()
            write_txt('phonebook.txt', phone_book)
            print("Данные скопированы в другой файл.")

        choice = show_menu()

def copy_line():
    source_file = input('Введите имя файла, из которого нужно скопировать данные: ')
    dest_file = input('Введите имя файла, в который нужно скопировать данные: ')
    line_number = int(input('Введите номер строки, которую необходимо скопировать: '))

    source_phone_book = read_txt(source_file)
    dest_phone_book = read_txt(dest_file)

    if line_number <= len(source_phone_book):
        record_to_copy = source_phone_book[line_number - 1]
        dest_phone_book.append(record_to_copy)
        write_txt(dest_file, dest_phone_book)
        print("Данные успешно скопированы.")
    else:
        print("Некорректный номер строки.")

def show_menu():
    print("\nВыберите необходимое действие:\n"
          "1. Отобразить весь справочник\n"
          "2. Найти абонента по фамилии\n"
          "3. Найти абонента по номеру телефона\n"
          "4. Добавить абонента в справочник\n"
          "5. Сохранить справочник в текстовом формате\n"
          "6. Скопировать строку в другой файл\n"
          "7. Закончить работу")
    choice = int(input())
    return choice

def read_txt(filename):
    phone_book = []
    fields = ['Фамилия', 'Имя', 'Отчество', 'Телефон']
    try:
        with open(filename, 'r', encoding='utf-8') as phb:
            for line in phb:
                record = dict(zip(fields, line.strip().split(',')))
                phone_book.append(record)
    except FileNotFoundError:
        print(f"Файл {filename} не найден. Создан новый справочник.")
    return phone_book

def write_txt(filename, phone_book):
    with open(filename, 'w', encoding='utf-8') as phout:
        for record in phone_book:
            s = ','.join(record.values())
            phout.write(f'{s}\n')

def print_result(phone_book):
    for record in phone_book:
        print(', '.join(record.values()))

def find_by_lastname(phone_book, last_name):
    result = [record for record in phone_book if record['Фамилия'].lower() == last_name.lower()]
    return result if result else "Абонент не найден."

def find_by_number(phone_book, number):
    result = [record for record in phone_book if record['Телефон'] == number]
    return result if result else "Абонент не найден."

def add_user(phone_book, user_data):
    fields = ['Фамилия', 'Имя', 'Отчество', 'Телефон']
    new_record = dict(zip(fields, user_data.split()))
    phone_book.append(new_record)

work_with_phonebook()
