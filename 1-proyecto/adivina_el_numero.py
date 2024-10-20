import random

def adivinador_numero():
    print("Piensa en un número entre 1 y 10.")

    # Adivinanza inicial
    adivinanza = random.randint(1, 10)
    print(f"¿Es {adivinanza} tu número?")

    # Loop para hacer preguntas hasta adivinar el número
    while True:
        respuesta = input("Ingresa 's' si es correcto, 'm' si tu número es más grande, 'n' si tu número es más pequeño: ")

        if respuesta == 's':
            print("¡Adiviné tu número!")
            break
        elif respuesta == 'm':
            adivinanza = random.randint(adivinanza + 1, 10)
        elif respuesta == 'n':
            adivinanza = random.randint(1, adivinanza - 1)
        else:
            print("Respuesta no válida. Ingresa 's', 'm' o 'n'.")

        print(f"¿Es {adivinanza} tu número?")

# Ejecutar el juego
adivinador_numero()
