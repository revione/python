import asyncio
import websockets
import spacy
import json

# Cargar el modelo de procesamiento del alemán
nlp = spacy.load("de_core_news_md")

async def enviar_mensaje(websocket, mensaje):
    # Crear un diccionario que contiene el mensaje
    mensaje_json = {"mensaje_servidor": mensaje}

    # Convertir el diccionario a una cadena JSON
    mensaje_json_str = json.dumps(mensaje_json)

    # Enviar el mensaje JSON al cliente
    await websocket.send(mensaje_json_str)

async def procesar_y_responder(websocket, mensaje):
    # Procesar el texto con SpaCy
    doc = nlp(mensaje)

    # Crear una lista de diccionarios con información de cada token
    tokens_info = []
    for token in doc:
        token_info = {
            "text": token.text,
            "pos": token.pos_,
            "tag": token.tag_,
            "morph": token.morph
        }
        tokens_info.append(token_info)

    # Crear un diccionario que contiene la lista de tokens
    respuesta_json = {"tokens": tokens_info}

    # Convertir el diccionario a una cadena JSON
    respuesta_json_str = json.dumps(respuesta_json)

    # Enviar la respuesta JSON al cliente
    await websocket.send(respuesta_json_str)

async def websocket_handler(websocket, path):
    try:
        while True:
            mensaje = await websocket.recv()
            print(f"Mensaje recibido: {mensaje}")

            # Procesar el mensaje y enviar la respuesta JSON
            await procesar_y_responder(websocket, mensaje)

            # Enviar un mensaje adicional al cliente
            await enviar_mensaje(websocket, "¡Hola desde el servidor!")

    except websockets.exceptions.ConnectionClosedError:
        print("La conexión se cerró inesperadamente.")

start_server = websockets.serve(websocket_handler, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
