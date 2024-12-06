chose = input("""Введите тип: 'по строчно', 'целое'
>>> """)
try:
    with open('example.txt', 'r') as file:
        if chose == "по строчно":
            for line in file:
                print(line, end = "\n")
        elif chose == "целое":
            content = file.read()
            print(content)
        else:
            print("такого типа нет")
except FileNotFoundError:
    print("извините такого файла нет. ")