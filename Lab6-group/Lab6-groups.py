"""
Словник 

номер групи; кнз-41с
прізвище, ім'я та по батькові; 
курс; комп'ютерні науки;
предмети та оцінки за семестр. 
"""

students = { 
     1: {
        'group': "КНЗ-41С",
        'surname': "Коваленко",
        'name': "Федор",
        'patronymic': "Олександрович",
        'course': 2,
        'major': "Комп'ютерні науки",
        'subjects': {'Математика': 88, 'Програмування': 95, 'Фізика': 78}
    },
    2: {
        'group': "КНЗ-41С",
        'surname': "Петрова",
        'name': "Марія",
        'patronymic': "Іванівна",
        'course': 1,
        'major': "Комп'ютерні науки",
        'subjects': {'Математика': 92, 'Програмування': 85, 'Англійська': 90}
    },
    3: {
        'group': "КНЗ-41С",
        'surname': "Левченко",
        'name': "Олена",
        'patronymic': "Сергіївна",
        'course': 2,
        'major': "Комп'ютерні науки",
        'subjects': {'Математика': 72, 'Програмування': 70, 'Англійська': 98}
    }
}

# Виведення на екран всіх значень словника
def print_all():
    print("\nВсі записи словника:")
    print("{:<4} {:<10} {:<10} {:<15} {:<6} {:<23} {:<}".format(
        "ID", "Прізвище", "Ім'я", "По батькові", "Курс", "Група", "Предмети(оцінки)\n"))
    for sid, info in students.items():
        subj = ", ".join(f"{k}:{v}" for k, v in info['subjects'].items())
        print(f"{sid:<4} {info['surname']:<10} {info['name']:<10} {info['patronymic']:<15} "
              f"{info['course']:<6} {info['group']:<10} {subj}")

def add_student():
    try:
        key = int(input("Введіть новий ключ (ID): ").strip())
    except ValueError:
        print("Невірний формат ключа. Потрібно ціле число.")
        return

    if key in students:
        print("Помилка: ключ вже існує!")
        return

    surname = input("Прізвище: ").strip()
    name = input("Ім'я: ").strip()
    patronymic = input("По батькові: ").strip()

    try:
        course = int(input("Курс: ").strip())
    except ValueError:
        print("Невірний формат курсу. Потрібно ціле число.")
        return

    group = input("Група: ").strip()
    major = input("Спеціальність (за замовчуванням 'Комп'ютерні науки'): ").strip() or "Комп'ютерні науки"

    subjects = {}
    print("Введіть предмети та оцінки (порожній предмет — завершити):")
    while True:
        subj = input("  Предмет: ").strip()
        if not subj:
            break
        try:
            grade = int(input("  Оцінка (0-100): ").strip())
        except ValueError:
            print("  Невірна оцінка — пропускаємо цей предмет.")
            continue
        subjects[subj] = grade

    students[key] = {
        'group': group,
        'surname': surname,
        'name': name,
        'patronymic': patronymic,
        'course': course,
        'major': major,
        'subjects': subjects
    }
    print(f"Запис додано успішно: {key}: {students[key]}")


if __name__ == "__main__":
    print_all()