# Знайти та роздрукувати ряд Фібоначчі з 5-го по 25-й елемент та підрахувати їх кількість

fib = [0, 1]
while len(fib) < 25:
    last_value = fib[-1] # fib[-1] — останній елемент списку
    before_last_value = fib[-2] # fib[-2] — передостанній елемент

    next_value = last_value + before_last_value
    fib.append(next_value) 
                           
"""
0 1
0 1 1
0 1 1 2
0 1 1 2 3 -> 5 елемент, iндекс 4
0 1 1 2 3 5
0 1 1 2 3 5 8
"""

fibs = fib[4:]  # 5-й - 25-й (індекс 4 - 24) 25 не потрапляє в діапазон
print("Ряд Фібоначчі з 5-го по 25-й елемент:")
for number in fibs:
    print(number)
# for i in range(len(fibs)):
#     print(fibs[i])
print("Кількість чисел:", len(fibs))

