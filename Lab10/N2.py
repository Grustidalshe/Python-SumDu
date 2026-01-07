import matplotlib.pyplot as plt
import numpy as np

# Роки спостережень
years = [
    2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013,
    2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023
]

# умовні дані
ukraine = [
    120000, 115000, 110000, 105000, 100000,
    98000, 95000, 92000, 90000, 88000,
    86000, 84000, 82000, 80000, 78000,
    76000, 74000, 72000, 70000, 68000
]

usa = [
    650000, 640000, 630000, 620000, 610000,
    600000, 590000, 580000, 570000, 560000,
    550000, 540000, 530000, 520000, 510000,
    500000, 490000, 480000, 470000, 460000
]

# === 2.1 Лінійний графік ===
plt.figure()
plt.plot(years, ukraine, label='Ukraine')
plt.plot(years, usa, label='USA')

plt.title('Children out of school, primary')
plt.xlabel('Year')
plt.ylabel('Number of children')
plt.legend()
plt.grid(True)
plt.show()

# === 2.2 Стовпчаста діаграма ===
country = input("Enter country (Ukraine or USA): ")

if country == "Ukraine":
    data = ukraine
elif country == "USA":
    data = usa
else:
    print("Incorrect country name")
    exit()

plt.figure()
plt.bar(years, data)
plt.title(f'Children out of school, primary – {country}')
plt.xlabel('Year')
plt.ylabel('Number of children')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()
