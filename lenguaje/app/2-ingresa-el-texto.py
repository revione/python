import spacy

def procesar_texto(texto):
    # Cargar el modelo de procesamiento del alemán
    nlp = spacy.load("de_core_news_md")

    # Procesar el texto
    doc = nlp(texto)

    # Iterar sobre cada token en la oración
    for token in doc:
        print(token.text, spacy.explain(token.pos_), token.tag_, token.morph)

# Bucle principal
while True:
    # Solicitar al usuario que ingrese el texto
    texto_usuario = input("Ingrese el texto que desea procesar (o 'salir' para terminar): ")

    # Verificar si el usuario quiere salir
    if texto_usuario.lower() == 'salir':
        break

    # Llamar a la función para procesar el texto
    procesar_texto(texto_usuario)