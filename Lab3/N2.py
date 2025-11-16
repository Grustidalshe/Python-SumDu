"""
Задано слово. Визначити суму ASCII кодів символів слова.
"""

a = str(input("Введіть слово: "))

# Обчислення суми ASCII кодів символів
sum_ascii = sum(ord(char) for char in a)
print("Сума ASCII кодів символів слова:", sum_ascii)
