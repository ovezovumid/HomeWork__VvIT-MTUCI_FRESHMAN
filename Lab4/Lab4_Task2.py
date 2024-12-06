import my_module
try:
    x, y = int(input("Введите первое число: ")), int(input("Введите второе число: "))
    print(my_module.my_module_sum(x, y))
except ValueError:
    print("Вы ввели не число!")