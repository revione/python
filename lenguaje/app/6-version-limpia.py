import asyncio
import websockets
import spacy
import json

nlp = spacy.load("de_core_news_md")

async def procesar_y_responder(websocket, mensaje):
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

async def websocket_handler(websocket, path):
    try:
        while True:
            mensaje_str = await websocket.recv()

            try:
                mensaje = json.loads(mensaje_str)
            except json.JSONDecodeError as e:
                print(f"Error al decodificar la cadena JSON: {e}")

            mensaje_texto = mensaje.get("mensaje", "")

            await procesar_y_responder(websocket, mensaje_texto)

    except websockets.exceptions.ConnectionClosedOK:
        print("La conexión se cerró de manera ordenada.")

    except websockets.exceptions.ConnectionClosedError:
        print("La conexión se cerró inesperadamente.")


start_server = websockets.serve(websocket_handler, "localhost", 8765)
print('\nServidor corriendo\n\n')
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
