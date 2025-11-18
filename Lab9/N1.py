import csv

import os

flag = False

#Вивід всього файлу
def open_file():

    try:

        csvfile = open("exports-of-goods-and-services.csv","r", encoding="utf-8") 

        reader = csv.DictReader(csvfile, delimiter = ",")

        print("Country Name: 2015 [YR2015] | 2019 [YR2019]")

        for row in reader:

            print(row['Country Name'], ': ', row["2015 [YR2015]"], row["2019 [YR2019]"])
        csvfile.close()

    except FileNotFoundError:
        print("Файл exports-of-goods-and-services.csv не знайдено!")
        return False

    return True

#Пошук по країні
def search_country():
    try:
        with open("exports-of-goods-and-services.csv", "r", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)

            indicator = input("\nВведіть назву країни для пошуку: ").strip()

            # Валідація
            while indicator.isnumeric():
                indicator = input("Некоректно! Введіть назву країни: ").strip()

            found = False

            for row in reader:
                if row["Country Name"].lower() == indicator.lower():
                    found = True

                    print("\nЗнайдено дані:")
                    print("-----------------------------------")
                    print(
                        f"{row['Country Name']}: {row['2015 [YR2015]']} (2015), {row['2019 [YR2019]']} (2019)"
                    )

                    # Запис результату в новий CSV
                    csvfile2 = open("found_countries.csv", "a", encoding="utf-8", newline="")
                    writer = csv.writer(csvfile2, delimiter=";")
                    writer.writerow([
                            row["Country Name"],
                            row["2015 [YR2015]"],
                            row["2019 [YR2019]"]
                        ])
                    csvfile2.close()
                    print("\nРезультат записано у found_countries.csv")
                    break

            if not found:
                print(f"\nДані для країни '{indicator}' не знайдено!")

    except FileNotFoundError:
        print("Файл exports-of-goods-and-services.csv не знайдено!")


if __name__ == "__main__":

    if open_file():
        while True:             
            search_country()
            cont = input("\nБажаєте виконати ще один пошук? (так/ні): ").strip().lower()
            if cont == 'ні':
                print("Вихід з програми.")
                break