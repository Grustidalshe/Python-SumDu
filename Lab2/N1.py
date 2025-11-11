import math

# z=sin(α+β)∗sin(α−β)

def expression(a, b):
    z = math.sin(a + b) * math.sin(a - b)
    return z

"""  
Спортсмен пробігає за 1-й день М км, кожний наступний день він збільшує норму пробігу на К%.
Визначите через скільки днів норма пробігу може стати більше 50 км.
"""

def athlet(m, k):
    day = 0
    percent = k / 100

    max_km = 50
    while not (m > max_km):
        delta = m * percent
        m += delta
        day += 1

    return day

print("Задача 1")
a = int(input("Введіть ціле число α: "))
b = int(input("Введіть ціле число β: "))

result = expression(a, b)
print(result)

print("\nЗадача 2")
m = int(input("Введіть ціле число m: "))
k = int(input("Введіть ціле число k: "))

result = athlet(m, k)

print(f"Норма пробігу стала більше за 50 км через {result} дні")