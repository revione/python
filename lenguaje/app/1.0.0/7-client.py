import asyncio
import websockets
import json

async def enviar_mensaje():
    async with websockets.connect("ws://localhost:8765") as websocket:
    # async with websockets.connect("ws://localhost:4433") as websocket:
    # async with websockets.connect("ws://192.168.1.100:8765") as websocket:
    # async with websockets.connect("ws://0.0.0.0:87655") as websocket:
        
        mensaje = {
            "mensaje": "Guten Tag! Ich hoffe, das funktioniert gut."
        }
        mensaje_json = json.dumps(mensaje)
        await websocket.send(mensaje_json)
        print(f"Mensaje enviado: {mensaje_json}")

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(enviar_mensaje())

