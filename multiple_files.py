from utils import *
mensaje = input("Please type your message\n")
codificado = flip(mensaje) + str(count_letters(mensaje, 'a'))
print(f"Your encoded message is: {codificado}")