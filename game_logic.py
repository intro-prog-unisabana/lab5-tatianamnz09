from secret_number import seed_secret_numbers, generate_secret_number
from response import input_response

seed = int(input("Enter a seed number:\n"))
seed_secret_numbers(seed)
numero_secreto = generate_secret_number()

intentos = 0
adivinado = False

while not adivinado:
    guess = int(input("What is your guess:\n"))
    intentos += 1
    mensaje, adivinado = input_response(numero_secreto, guess)
    print(mensaje)

print(f"It took you {intentos} tries!")