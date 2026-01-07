import matplotlib.pyplot as plt
import json
import os

# Ім'я файлу JSON
json_filename = 'exports_data.json'

# --- БЛОК 1: Створення тестового JSON файлу (щоб код працював одразу) ---
# Ми беремо дані з вашого прикладу CSV та записуємо їх у форматі JSON
raw_data = [
    {"Country Name": "Albania", "Code": "ALB", "Value_2019": "30.94"},
    {"Country Name": "Angola",  "Code": "AGO", "Value_2019": "40.79"},
    {"Country Name": "Ukraine", "Code": "UKR", "Value_2019": "41.23"},
    {"Country Name": "Zambia",  "Code": "ZMB", "Value_2019": "34.64"},
    {"Country Name": "Andorra", "Code": "AND", "Value_2019": ".."}  # Приклад відсутніх даних
]

with open(json_filename, 'w', encoding='utf-8') as f:
    json.dump(raw_data, f, ensure_ascii=False, indent=4)

print(f"Файл '{json_filename}' успішно створено для тестування.\n")


# --- БЛОК 2: Основна програма (Зчитування та Побудова) ---

def plot_exports_pie_chart(filename):
    try:
        # 1. Зчитування даних з JSON файлу
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)

        countries = []
        values = []

        # 2. Обробка даних
        print("Обробка даних:")
        for entry in data:
            country = entry.get('Country Name')
            val_str = entry.get('Value_2019')

            # Перевірка: чи є значення і чи воно не є порожнім ("..")
            if val_str and val_str != "..":
                try:
                    val_float = float(val_str)
                    countries.append(country)
                    values.append(val_float)
                    print(f" -> Додано: {country} ({val_float})")
                except ValueError:
                    print(f" -> Помилка конвертації для {country}")
            else:
                print(f" -> Пропущено (немає даних): {country}")

        # Якщо даних немає, графік не будуємо
        if not values:
            print("Немає коректних даних для побудови графіка.")
            return

        # 3. Налаштування кольорів та оформлення
        # Генеруємо кольори або задаємо вручну
        colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']
        
        # Виділяємо (explode) найбільший сектор
        max_val_index = values.index(max(values))
        explode = [0] * len(values)
        explode[max_val_index] = 0.1  # "Висунути" лідера на 10%

        # 4. Побудова кругової діаграми
        plt.figure(figsize=(10, 7))
        
        wedges, texts, autotexts = plt.pie(
            values,
            explode=explode,
            labels=countries,
            colors=colors[:len(values)], # Беремо стільки кольорів, скільки країн
            autopct='%1.1f%%',           # Формат відсотків (один знак після коми)
            shadow=True,
            startangle=140
        )

        # Налаштування шрифту для відсотків, щоб було краще видно
        plt.setp(autotexts, size=10, weight="bold", color="black")
        plt.setp(texts, size=11)

        # 5. Оформлення
        plt.title('Експорт товарів та послуг (% від ВВП) за 2019 рік\n(порівняння вибраних країн)', fontsize=14)
        plt.axis('equal') # Щоб діаграма була круглою, а не овальною

        # 6. Вивід
        plt.show()

    except FileNotFoundError:
        print(f"Файл {filename} не знайдено!")
    except json.JSONDecodeError:
        print(f"Помилка структури JSON у файлі {filename}")

# Запуск функції
if __name__ == "__main__":
    plot_exports_pie_chart(json_filename)