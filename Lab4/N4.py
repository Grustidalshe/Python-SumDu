"""
Пошук середнього арифметичного від'ємних елементів масиву.

"""


def average():

    A = list(map(int,input('Введіть елементи списку через пробіл: ').split()))

    print(A)

    negative_elements = [x for x in A if x < 0]
    if negative_elements:
        avr = sum(negative_elements) / len(negative_elements) # ділення на кількість від'ємних елементів
    else:
        avr = 0 # Якщо від'ємних елементів немає, середнє арифметичне дорівнює 0

    print ('Середнє арифметичне від\'ємних елементів:',avr)

    return avr 

average()