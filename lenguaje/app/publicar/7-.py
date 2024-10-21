import asyncio
import websockets
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

nlp = spacy.load("de_core_news_md")

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
        while True:
            mensaje_str = await websocket.recv()

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
host = os.getenv("WEBSOCKET_HOST", "127.0.0.1")
port = int(os.getenv("WEBSOCKET_PORT", 8765))

# Función para arrancar el servidor
async def start_websocket_server():
    start_server = await websockets.serve(websocket_handler, host, port)
    return start_server

# Aplicación principal que ejecuta el servidor WebSocket
async def main():
    server = await start_websocket_server()

    try:
        await asyncio.Future()  # Mantener el servidor corriendo indefinidamente
    except asyncio.CancelledError:
        logger.info("Servidor WebSocket detenido.")
    except KeyboardInterrupt:
        logger.info("Servidor detenido manualmente por el usuario.")
    except Exception as e:
        logger.error(f"Error inesperado: {e}")
    finally:
        logger.info("Cerrando el servidor WebSocket...")
        server.close()
        await server.wait_closed()
        logger.info("Servidor WebSocket cerrado.")

# Ejecuta el bucle de eventos usando asyncio.run()
if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Interrupción manual del programa (Ctrl+C).")
