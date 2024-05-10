import asyncio
from websockets.server import serve
import random
from helpers import is_prime ,is_primitive

async def echo(websocket):
       pass
        

async def main():
    async with serve(echo,"localhost", 8765):
        file_path = './public.txt'

        q = 0
        while (not is_prime(q)):
            q = random.randint(1,1000)

        a = random.randint(1,q)
        while ( not is_primitive(a,q)):
            a = random.randint(1,q)

        with open(file_path, 'w') as file:
            file.write('q = ' + str(q) + '\n')
            file.write('a = ' + str(a) + '\n')

        await asyncio.Future()  # run forever

asyncio.run(main())