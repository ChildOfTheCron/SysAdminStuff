#!/usr/bin/env python3.6

#WS server example

import asyncio
import websockets

async def hello(websocket, path):
	name = await websocket.recv()
	print(f"< {name}")

	greeting = f"Hello client {name}!"

	await websocket.send(greeting)
	print(f"> {greeting}")

start_server = websockets.serve(hello, '10.0.2.12', 8444)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

