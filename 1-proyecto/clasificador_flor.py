# Programa simple de inteligencia artificial para clasificar flores por color

def clasificar_flor(color):
    if color == "rojo":
        return "La flor es una rosa."
    elif color == "azul":
        return "La flor es una violeta."
    elif color == "amarillo":
        return "La flor es una margarita."
    else:
        return "No estoy seguro de qué tipo de flor es."

# Obtener el color de la flor del usuario
color_flor = input("Ingresa el color de la flor: ")

# Clasificar la flor y mostrar el resultado
resultado = clasificar_flor(color_flor)
print(resultado)
