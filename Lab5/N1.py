"""
виведення на екран всіх значень словника;
додавання (видалення) нового запису до (зі) словника;
перегляд вмісту словника за відсортованими ключами 
(перетворити об‘єкт подання ключів в список або скористатися функцією sorted,
застосувавши її до словника, або об‘єкту, який повертає метод keys)

Задано дані про n=10 учнів кількох шкіл, які займаються в гуртку з робототехніки 
(прізвище, ім'я, адреса, номер школи і клас). Скласти програму, яка визначає прізвище, 
ім'я та адресу учнів, що навчаються у визначеній школі в старших (10-11) класах,
ці дані записати в окремий масив – список з елементами типу «ключ: кортеж».
"""

students = {
    1: ("Іванов", "Олег", "вул. Шевченка 10", 12, 9),
    2: ("Петрова", "Марія", "вул. Франка 5", 15, 10),
    3: ("Сидоренко", "Анна", "вул. Лесі Українки 3", 12, 11),
    4: ("Коваль", "Богдан", "вул. Грушевського 20", 18, 8),
    5: ("Тимченко", "Ірина", "вул. Київська 7", 12, 10),
    6: ("Гнатюк", "Василь", "вул. Набережна 1", 15, 7),
    7: ("Швець", "Олексій", "вул. Садова 12", 18, 11),
    8: ("Мельник", "Юлія", "вул. Дніпровська 14", 15, 9),
    9: ("Мороз", "Катерина", "вул. Квіткова 8", 12, 11),
    10: ("Маслюк", "Денис", "вул. Сонячна 2", 18, 10),
}

# Виведення на екран всіх значень словника
def print_all():
    print("\nВсі записи словника:")
    for key, value in students.items():
        print(f"{key}: {value}")

# Додавання нового запису
def add_student():
    try:
        key = int(input("Введіть новий ключ (ID): ").strip())
        if key in students:
            print("Помилка: ключ вже існує!")
            return
        surname = input("Прізвище: ").strip()
        name = input("Ім'я: ").strip()
        address = input("Адреса: ").strip()
        school = int(input("Номер школи: ").strip())
        grade = int(input("Клас: ").strip())
        students[key] = (surname, name, address, school, grade)
        print(f"Запис додано успішно: {key}: {students[key]}")
    except ValueError:
        print("Помилка: неправильний формат даних!")

# Видалення запису
def remove():
    try:
        key = int(input("Введіть число запису яке потрібно видалити: ").strip())
    except ValueError:
        print("Ключ повинен бути числом.")
        return
    if key in students:
        del students[key]
        print(f"Видалено запис з ключем: {key}")
    else:
        print(f"Запис з ключем {key} не знайдено.")

# Перегляд вмісту словника за відсортованими ключами
def sorted_keys():
    print("\nЗаписи за відсортованими школами:")
        # сортування за школою → за прізвищем
    items = sorted(students.values(), key=lambda v: (v[3], v[0]))

    for prizv, name, addr, sch, gr in items:
        print(f'{sch}, "{prizv}", "{name}", {gr}')

# Фільтрація учнів за номером школи та класами 10-11
def filterSchool_students():
    """Фільтрація учнів за номером школи та класами 10-11; повертає список (key, (prizv,name,addr))."""
    try:
        school = int(input("Введіть номер школи для пошуку: ").strip())
    except ValueError:
        print("Помилка: номер школи повинен бути числом!")
        return

    result_list = []

    for key, data in students.items():
        prizv, name, addr, sch, gr = data
        if sch == school and gr in (10, 11):
            result_list.append((key, (prizv, name, addr)))

    # Сортування результату за прізвищем5
    result_list.sort(key=lambda x: x[1][0])
    
    if result_list:
        print("\nУчні старших класів цієї школи:\n")
        print(f"{'ID':<4} {'Прізвище':<15} {'Ім\'я':<7} {'Адреса':<35}")
        print("-" * 37)
        for key, (prizv, name, addr) in result_list:
            print(f"{key:<4} {prizv:<15} {name:<7} {addr:<35}")
    else:
        print("Учнів знайдено не було.")

    print("\nРезультуючий список:")
    for key, (prizv, name, addr) in result_list:
        print(f"{key} – {prizv}, {name}, {addr}")


def menu():
    while True:
        print("\n--------------- М Е Н Ю ---------------")
        print("1 – Вивести всі записи")
        print("2 – Додати запис")
        print("3 – Видалити запис")
        print("4 – Переглянути словник за відсортованими школами")
        print("5 – Фільтрація учнів за школою і класами 10-11")
        print("0 – Вихід")

        choice = input("Оберіть пункт меню: ").strip()

        if choice == "1":
            print_all()
        elif choice == "2":
            add_student()
        elif choice == "3":
            remove()
        elif choice == "4":
            sorted_keys()
        elif choice == "5":
            filterSchool_students()
        elif choice == "0":
            print("Роботу завершено.")
            break
        else:
            print("Невідома команда! Спробуйте ще.")

if __name__ == "__main__":
    menu()
