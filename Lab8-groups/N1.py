import os

# Назва спільного файлу
FILENAME = "Лабораторна8-групова.txt"

# Функції для роботи з файлом

def create_file(student_surname, question):
    """Створює файл і записує перше питання."""
    with open(FILENAME, "w", encoding="utf-8") as f:
        f.write("--------------------------------\n")
        f.write(f"Student: {student_surname}\n")
        f.write(f"Role: Question\n")
        f.write(f"Content: {question}\n")
        f.write("--------------------------------\n")
    print(f"Файл створено студентом {student_surname}")

def add_reply(student_surname, answer, next_question):
    """Додає відповідь і нове питання в кінець файлу."""
    # Перевірка наявності файлу
    if not os.path.exists(FILENAME):
        print("Помилка: Файлу не існує. Спочатку запустіть create_file.")
        return

    with open(FILENAME, "a", encoding="utf-8") as f:
        f.write(f"Student: {student_surname}\n")
        f.write(f"Role: Answer & New Question\n")
        f.write(f"Answer: {answer}\n")
        f.write(f"Next Question: {next_question}\n")
        f.write("--------------------------------\n")
    print(f"Відповідь додано студентом {student_surname}")

def read_file():
    """читає і показує файл."""
    if os.path.exists(FILENAME):
        print("\n---------- ВМІСТ ФАЙЛУ ---------")
        with open(FILENAME, "r", encoding="utf-8") as f:
            print(f.read())
        print("----------------------------------\n")
    else:
        print("Файл ще не створено")

if __name__ == "__main__":
    
    # Трубіна — створює файл
    if os.path.exists(FILENAME):
        os.remove(FILENAME) 
    
    create_file(
        student_surname="Trubina", 
        question="Як відкрити та прочитати файл у Python?"
    )

    # Петренко — дає відповідь і питає далі
    add_reply(
        student_surname="Petrenko",
        answer="Треба використати конструкцію with open(name, 'r') as f.",
        next_question="Як обробляти помилки (наприклад, якщо файлу немає)?"
    )

    # Сидоренко — дає відповідь і питає далі
    add_reply(
        student_surname="Sydorenko",
        answer="Для обробки помилок використовують блок try - except.",
        next_question="Як записати список рядків у файл однією командою?"
    )

    # Перевірка результату
    read_file()