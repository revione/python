def asistente_decisiones():
    print("¡Bienvenido al Asistente de Decisiones!")

    # Pregunta inicial
    decision = input("¿Deberías tomar una decisión importante ahora? (s/n): ")

    # Toma de decisiones basada en la respuesta
    if decision.lower() == 's':
        print("¡Entonces, vamos a pensar en eso!")
        opciones = input("¿Cuáles son las opciones que estás considerando? (Separadas por comas): ")
        opciones_lista = [opcion.strip() for opcion in opciones.split(',')]

        # Pregunta al usuario sobre las opciones
        print(f"Genial, tienes las siguientes opciones: {opciones_lista}")
        eleccion = input("¿Tienes una preferencia entre estas opciones? (Ingresa el número de la opción): ")

        # Toma de decisión final
        print(f"Después de considerar tus opciones, el Asistente de Decisiones sugiere: '{opciones_lista[int(eleccion)-1]}'.")
    else:
        print("¡No hay decisiones importantes por ahora! ¡Hasta luego!")

# Ejecutar el asistente
asistente_decisiones()
