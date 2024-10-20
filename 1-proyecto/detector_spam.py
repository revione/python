def clasificador_spam(mensaje):
    # Lista de palabras clave asociadas con spam
    palabras_spam = ["oferta", "ganador", "gratis", "urgente", "premio", "herencia"]

    # Tokeniza el mensaje en palabras
    palabras_en_mensaje = mensaje.lower().split()

    # Muestra las palabras en el mensaje
    print("Palabras en el mensaje:", palabras_en_mensaje)

    # Comprueba si hay alguna palabra clave en el mensaje
    for palabra in palabras_spam:
        if palabra in palabras_en_mensaje:
            return "¡Alerta! Este mensaje podría ser spam."

    # Si no se encontraron palabras clave, el mensaje probablemente no es spam
    return "Este mensaje parece ser legítimo."

# Obtener el mensaje del usuario
mensaje_usuario = input("Ingresa tu mensaje: ")

# Clasificar el mensaje y mostrar el resultado
resultado = clasificador_spam(mensaje_usuario)
print(resultado)
