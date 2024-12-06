def max_of_two(x, y):

    return x if x > y else y


number1 = int(input("Input first number: "))
number2 = int(input("Input second number: "))
result = max_of_two(number1, number2)
print(f"Larger number: {result}")
