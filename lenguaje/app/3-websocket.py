import asyncio
import websockets

async def websocket_handler(websocket, path):
    try:
        while True:
            mensaje = await websocket.recv()
            print(f"Mensaje recibido: {mensaje}")

            respuesta = f"Recibí tu mensaje: {mensaje}"
            await websocket.send(respuesta)

    except websockets.exceptions.ConnectionClosedError:
        print("La conexión se cerró inesperadamente.")

start_server = websockets.serve(websocket_handler, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
