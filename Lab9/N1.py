import csv
import os

NO_DATA = ".."

#
def read_file(path, var_name):
    try:
        with open(path, "r", encoding="utf-8") as csvfile: #відкриття файлу для читання

            reader = csv.DictReader(csvfile, delimiter=",")

            datos = []
        
            for row in reader:
                if row["Series Name"] == var_name:
                    datos.append(row)

            print(f'Знайдено {len(datos)} записів для змінної "{var_name}"\n')
            return datos               
        
    except FileNotFoundError:
        print(f"Файл {path} не знайдено!")


def print_data(datos):
    """
    datos = [
       {
        "Series Name": "Exports of goods and services (% of GDP)",
        "Series Code": "NE.EXP.GNFS.ZS",
        "Country Name": "Albania",
        "Country Code": "ALB",
        "2015 [YR2015]": "27.0693224620319",
        "2019 [YR2019]": "30.9361224858484"
        },
       {},
       {},
    ]

    Распечатать название страны, значение за 2015 год, значение за 2019 год
    """

    print("Country Name: 2015 [YR2015], 2019 [YR2019]")
    for data in datos:
        country_name = data["Country Name"]
        y2015 = data["2015 [YR2015]"]
        y2019 = data["2019 [YR2019]"]
        print(f"{country_name}: {y2015}, {y2019}")
        

def get_countries(allowed_countries):
    """
    allowed_countries = ['Albania', ... , 'Zambia']
    """
    countries = []
    stop = False
    stop_word = 'no'
    while not stop:
        country = input(f"\nНапишить назву країни (або '{stop_word}' для виходу): ")

        if country == stop_word:
            stop = True

        elif country in allowed_countries:
            countries.append(country)

        else:
            print('\nТака назва відсутня.')

    return countries


#Пошук по країні
def search_by_countries(countries, datos):
    """
    Из всех данных (datos) оставить только те, у которых значение Country Name содержится в списке искомых стран (countries)

    countries = ['Albania', 'Zambia']

    datos = [
       {
        "Series Name": "Exports of goods and services (% of GDP)",
        "Series Code": "NE.EXP.GNFS.ZS",
        "Country Name": "Albania",
        "Country Code": "ALB",
        "2015 [YR2015]": "27.0693224620319",
        "2019 [YR2019]": "30.9361224858484"
        },
       {},
       {},
    ]
    """
    # result = [data for data in datos if data["Country Name"] in countries]
    
    result = []

    for data in datos:
        country_name = data["Country Name"]

        if country_name in countries:
            result.append(data)

    return result


def save_file(path, filtered_datos, columns):
    """
    записати результат пошуку у новий .csv файл

    path = "filename.csv"

    filtered_datos = [
       {
        "Series Name": "Exports of goods and services (% of GDP)",
        "Series Code": "NE.EXP.GNFS.ZS",
        "Country Name": "Albania",
        "Country Code": "ALB",
        "2015 [YR2015]": "27.0693224620319",
        "2019 [YR2019]": "30.9361224858484"
        },
       {},
       {},
    ]

    columns = ["Country Name", "Country Code", "2015 [YR2015]", "2019 [YR2019]"]
    """
    with open(path, "w", encoding="utf-8", newline='') as result_file:
        writer = csv.DictWriter(result_file, fieldnames=columns, extrasaction='ignore')

        writer.writeheader()
        writer.writerows(filtered_datos)

    print(f"\nРезультат пошуку записан у файл {path}")



if __name__ == "__main__":

    var_name = "Exports of goods and services (% of GDP)"
    filename = "exports-of-goods-and-services.csv"

    # прочитать файл и положить в список отфильтрованые строки (в формате словаря)
    datos = read_file(path=filename, var_name=var_name)
    # распечатать полученые строки
    print_data(datos)
    # список названий стран которые есть в наших данных
    allowed_countries = [data['Country Name'] for data in datos]

    # получить от пользователя названия стран (список)
    countries = get_countries(allowed_countries)

    # отфильтровать данные по введенным пользователем странам
    result = search_by_countries(countries, datos)

    # сохранить результат в новый файл
    new_filename = f"search_result {var_name}.csv"
    columns = ["Country Name", "Country Code", "2015 [YR2015]", "2019 [YR2019]"]
    save_file(path=new_filename, filtered_datos=result, columns=columns)
