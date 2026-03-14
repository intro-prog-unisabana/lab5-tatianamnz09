from utils import *

operaciones_dos = ["add", "subtract", "multiply", "divide", "exponent", "modulo", "floor_divide"]
operaciones_uno = ["absolute"]

while True:
    op = input("Which calculation would you like to perform? (add, subtract, multiply, divide, exponent, modulo, floor_divide, absolute, exit):\n").lower()

    if op == "exit":
        break
    elif op in operaciones_dos:
        num1 = float(input("Enter the first number:\n"))
        num2 = float(input("Enter the second number:\n"))
        if op == "add":
            resultado = add(num1, num2)
        elif op == "subtract":
            resultado = sub(num1, num2)
        elif op == "multiply":
            resultado = multiply(num1, num2)
        elif op == "divide":
            resultado = divide(num1, num2)
        elif op == "exponent":
            resultado = exponent(num1, num2)
        elif op == "modulo":
            resultado = modulo(num1, num2)
        elif op == "floor_divide":
            resultado = floor_divide(num1, num2)
        print(f"The result is: {resultado}")
    elif op in operaciones_uno:
        num = float(input("Enter the number:\n"))
        resultado = absolute(num)
        print(f"The result is: {resultado}")
    else:
        print("Invalid option!")