# ...existing code...
"""
Задано дані про n=10 учнів кількох шкіл, які займаються в гуртку робототехніки 
(прізвище, ім'я, адреса, номер школи, день відвідування гуртка  - субота чи неділя). 
Скласти програму, яка визначає прізвище, ім'я та адресу учнів, що навчаються у молодших (7-8) класах 
та відвідують гурток по суботах.
"""
import json
import os
DATA_FILE = os.path.join(os.path.dirname(__file__), 'data.json')

initial_students = [
    {"Name":"Vasiliy","Surname":"Logvinov","Patronymic":"Antonovich","Adress":"Mira 5","School":9,"Class":6,"Day":"неділя"},
    {"Name":"Anton","Surname":"Lipovyi","Patronymic":"Andreevich","Adress":"Naberezhnaya 10","School":10,"Class":10,"Day":"субота"},
    {"Name":"Alina","Surname":"Popovich","Patronymic":"Viktorovna","Adress":"Pushkina 5","School":10,"Class":11,"Day":"неділя"},
    {"Name":"Iryna","Surname":"Petrenko","Patronymic":"Ivanivna","Adress":"Shevchenka 3","School":5,"Class":7,"Day":"субота"},
    {"Name":"Oksana","Surname":"Bondarenko","Patronymic":"Mykolaivna","Adress":"Lermontova 7","School":8,"Class":8,"Day":"субота"},
    {"Name":"Maksym","Surname":"Koval","Patronymic":"Petrovich","Adress":"Sovetskaya 12","School":3,"Class":7,"Day":"неділя"},
    {"Name":"Olena","Surname":"Kostenko","Patronymic":"Serhiivna","Adress":"Druzhby 4","School":6,"Class":8,"Day":"субота"},
    {"Name":"Dmytro","Surname":"Kuznetsov","Patronymic":"Olehovich","Adress":"Parkova 15","School":4,"Class":9,"Day":"субота"},
    {"Name":"Anna","Surname":"Melnyk","Patronymic":"Andriivna","Adress":"Gagarina 2","School":2,"Class":7,"Day":"субота"},
    {"Name":"Mykola","Surname":"Horban","Patronymic":"Ivanovich","Adress":"Soborna 1","School":1,"Class":8,"Day":"неділя"}
]

def load_students():
    if not os.path.exists(DATA_FILE):
        save_students(initial_students)
        return list(initial_students)
    try:
        with open(DATA_FILE, 'rt', encoding='utf-8') as f:
            return json.load(f)
    except Exception:
        return list(initial_students)

def save_students(students):
    with open(DATA_FILE, 'wt', encoding='utf-8') as f:
        json.dump(students, f, ensure_ascii=False, indent=2)

def find_young_sat_students(students):
    res = []
    for s in students:
        try:
            cls = int(s.get('Class', 0))
        except Exception:
            continue
        day = (s.get('Day') or '').strip().lower()
        if cls in (7, 8) and day in ('субота', 'sobota', 'saturday'):
            res.append((s.get('Surname',''), s.get('Name',''), s.get('Adress','')))
    return res

def add_student_interactive():
    students = load_students()
    print('Додавання учня:')
    name = input('Name: ').strip()
    surname = input('Surname: ').strip()
    patronymic = input('Patronymic: ').strip()
    adress = input('Adress: ').strip()
    try:
        school = int(input('School (number): ').strip())
    except Exception:
        school = 0
    try:
        cls = int(input('Class (number): ').strip())
    except Exception:
        cls = 0
    day = input('Day (субота/неділя): ').strip()
    students.append({
        "Name": name,
        "Surname": surname,
        "Patronymic": patronymic,
        "Adress": adress,
        "School": school,
        "Class": cls,
        "Day": day
    })
    save_students(students)
    print('Учень доданий.')

def show_all_students():
    students = load_students()
    for i, s in enumerate(students, 1):
        print(f"{i}. {s.get('Surname','')}, {s.get('Name','')} — {s.get('Adress','')} (School {s.get('School','')}, Class {s.get('Class','')}, Day {s.get('Day','')})")

def main():
    while True:
        print("\nМеню:\n 1 - Показати учнів 7-8 класів, що відвідують гурток у суботу\n 2 - Показати всі записи\n 3 - Додати учня\n 4 - Вихід")
        choice = input("Вибір: ").strip()
        if choice == '1':
            students = load_students()
            matches = find_young_sat_students(students)
            if not matches:
                print("Не знайдено учнів 7-8 класів, що відвідують гурток у суботу.")
            else:
                print("Прізвище, ім'я, адреса:")
                for surname, name, adress in matches:
                    print(f"{surname}, {name}, {adress}")
        elif choice == '2':
            show_all_students()
        elif choice == '3':
            add_student_interactive()
        elif choice == '4':
            break
        else:
            print("Невірний вибір, спробуйте ще раз.")

if __name__ == '__main__':
    main()
