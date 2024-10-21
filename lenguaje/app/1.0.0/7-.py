import asyncio
import websockets
import socket
import spacy
import json
import os
import logging
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Configuración del logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# nlp = spacy.load("de_dep_news_trf")
nlp = spacy.load("de_core_news_sm")

async def procesar_y_responder(websocket, mensaje):
    try:
        doc = nlp(mensaje)
        tokens_info = []

        for token in doc:
            token_info = {
                "text": token.text,
                "lemma": token.lemma_,
                "pos": token.pos_,
                "tag": token.tag_,
                "head": {
                    "text": token.head.text,
                    "pos": token.head.pos_,
                },
                "morph": token.morph.to_dict(),
            }
            tokens_info.append(token_info)

        respuesta_json = {"tokens": tokens_info}
        respuesta_json_str = json.dumps(respuesta_json)
        await websocket.send(respuesta_json_str)
    except Exception as e:
        logger.error(f"Error al procesar y responder: {e}")

async def websocket_handler(websocket, path):
    try:
        logger.info(f"Manejo de conexión iniciado en el path: {path}")
        print(f"Manejo de conexión iniciado en el path: {path}")

        while True:
            mensaje_str = await websocket.recv()
            print(f"Mensaje recibido: {mensaje_str}")

            try:
                mensaje = json.loads(mensaje_str)
            except json.JSONDecodeError as e:
                logger.error(f"Error al decodificar la cadena JSON: {e}")
                continue

            mensaje_texto = mensaje.get("mensaje", "")

            if not mensaje_texto:
                logger.warning("El mensaje no tiene el formato esperado.")
                continue

            await procesar_y_responder(websocket, mensaje_texto)

    except websockets.exceptions.ConnectionClosedOK:
        logger.info("La conexión se cerró de manera ordenada.")
    except websockets.exceptions.ConnectionClosedError:
        logger.warning("La conexión se cerró inesperadamente.")
    finally:
        logger.info("La conexión se cerró, realizando limpieza si es necesario.")

# Configuración de la dirección y el puerto desde variables de entorno
# host = os.getenv("WEBSOCKET_HOST", "0.0.0.0")
host = os.getenv("WEBSOCKET_HOST", "127.0.0.1")
port = int(os.getenv("WEBSOCKET_PORT", 8765))

logger.info(f'Servidor en {host}:{port}')
start_server = websockets.serve(websocket_handler, host, port, family=socket.AF_INET)
logger.info(f'Servidor corriendo en {host}:{port}')

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
