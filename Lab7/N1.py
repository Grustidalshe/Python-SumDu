"""
Розробити програму, яка: 
а) створює текстовий файл TF9_1 із символьних рядків різної довжини;
б) читає вміст файла TF9_1, формує рядки за правилом: якщо рядок файла TF1 коротший ніж 20 символів, 
то він доповнюється пробілами, а якщо довший, то зрізається, і записує їх у файл TF9_2; 
в) читає вміст файла TF9_2 і друкує його по рядках.

"""

def Open(file_name, mode):

    try:
        file = open(file_name, mode)

    except:
        print("Файл", file_name, "не вдалося відкрити!")
        return None

    else:
        print("Файл", file_name, "був відкритий!")
        return file

file1_name = "TF9_1.txt"
file2_name = "TF9_2.txt"

file_1_w = Open(file1_name, "w")

if(file_1_w != None):

    file_1_w.write("The numero\nIn world popularity euro\nMy Python program Folder\n")

    print("Інформація була успішно додана до TF9_2.txt!")

    file_1_w.close();
    print("\nФайл TF9_1.txt був закритий!")

file_2_r = Open(file1_name, "r") #  r -  відкриває файл для читання, покажчик знаходиться на початку файла

file_2_w = Open(file2_name, "w") #  w - відкриває файл для запису, якщо файла не існує, то він буде створений, якщо існує, то його вміст буде стертий


"""
читає вміст файла TF9_1, формує рядки за правилом: якщо рядок файла TF1 коротший ніж 20 символів, 
то він доповнюється пробілами, а якщо довший, то зрізається, і записує їх у файл TF9_2; 
"""
with file_2_r, file_2_w:

    for line in file_2_r:
        line = line.rstrip("\n")  # видаляємо символ нового рядка

        # Якщо менше 20 символів — додаємо пробіли
        if len(line) < 20:
            line = line.ljust(20)

        # Якщо більше — обрізаємо до 20
        elif len(line) > 20:
            line = line[:20]

        # Записуємо змінений рядок
        file_2_w.write(line + "\n")

    print("\nФайли були закриті!")

print("Отримано:")

file_r = Open(file2_name, "r")

if file_r != None:

    for line in file_r.read().split("\n"):
        print(line)

    print("Файл TF9_2.txt був закритий!")

    file_r.close()