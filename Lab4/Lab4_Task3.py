from Package.Algebra import divide, square, multiply
from Package.Geometry import square_area, square_perimeter, rectangle_area, rectangle_perimeter

num_1, num_2 = int(input("Введите число для вычислени: ")), int(input("Введите число для вычислени: "))
print(f"Операция деления {divide(num_1, num_2)}")
print(f"Операция умножения {multiply(num_1, num_2)}")
print(f"Операция квадратного корня {square(num_1), square(num_2)}")

a, b = int(input("Введите число для вычислени: ")), int(input("Введите число для вычислени: "))
print(f"Операция нахождения площади квадрата {square_area(a), square_area(b)}")
print(f"Операция нахождения периметра квадрата {square_perimeter(a), square_perimeter(b)}")
print(f"Операция нахождения площади прямоугольника {rectangle_area(a, b)}")
print(f"Операция нахождения периметра прямоугольинка {rectangle_perimeter(a, b)}")
