"""
Задано слово. Визначити суму ASCII кодів символів слова.
"""

a = str(input("Введіть слово: "))

# Обчислення суми ASCII кодів символів
sum_ascii = sum(a.encode('ascii'))
print("Сума ASCII кодів символів слова:", sum_ascii)
