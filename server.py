import asyncio
from websockets.server import serve
import random
from helpers import is_prime ,is_primitive
connected_clients = list()
async def echo(websocket):
    connected_clients.append(websocket)
    async for message in websocket:
        if (message == "initilization"):
            continue
        if len(connected_clients) > 1:
            if (websocket == connected_clients[0]):
                await connected_clients[1].send(message)
            else:
                await connected_clients[0].send(message)
        

async def main():
    async with serve(echo,"localhost", 8765):
        file_path = './public.txt'

        q_d = 0
        while (not is_prime(q_d)):
            q_d = random.randint(1,1000)

        a_d = random.randint(1,q_d)
        while ( not is_primitive(a_d,q_d)):
            a_d = random.randint(1,q_d)

       

        q_g = 0
        while (not is_prime(q_g)):
            q_g = random.randint(1,1000)

        a_g = random.randint(1,q_g)
        while ( not is_primitive(a_g,q_g)):
            a_g = random.randint(1,q_g)
            
        with open(file_path, 'w') as file:
            file.write('q_d = ' + str(q_d) + '\n')
            file.write('a_d = ' + str(a_d) + '\n')
            file.write('q_g = ' + str(q_g) + '\n')
            file.write('a_g = ' + str(a_g) + '\n')

        await asyncio.Future()  # run forever

asyncio.run(main())