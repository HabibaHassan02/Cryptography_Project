import websockets
import random
import asyncio
from DH import DH
from Elgamal import elgamalEncryption,elgamalgeneration,generateKey,elgamalEncryption, elgamalDecryption
import hashlib
from helpers import encrypt_aes, decrypt_aes

async def hello():
    file_path = 'public.txt'
    data_dict = {}
    with open(file_path, 'r') as file:

        content = file.readlines()  

        for line in content:
            key, value = line.strip().split('=')
            key = key.strip()
            value = int(value.strip())  
            data_dict[key] = value

    q_d = data_dict["q_d"]
    q_g = data_dict["q_g"]
    a_d = data_dict["a_d"]
    a_g = data_dict["a_g"]

    x_a_d,y_a_d = DH(q_d,a_d)

    async with websockets.connect("ws://localhost:8765") as websocket:
            y_a_g , X_a_g = elgamalgeneration(q_g, a_g)
            await websocket.send(str(y_a_g))
            y_b_g = await websocket.recv()
            k= generateKey(q_g)
            C1,C2 = elgamalEncryption(y_a_d, a_g, X_a_g, q_d, k)
            await websocket.send((str(y_a_d),"/",str(C1),"/",str(C2)))
            message = await websocket.recv()
            y_b_d,C1,C2 = message.split("/")
            v1,v2 = elgamalDecryption(int(y_b_d),int(C1), int(C2),  int(q_d) ,a_d)
            K_d = (int(y_b_d)**x_a_d)%q_d
            sha256_hash = hashlib.sha256()
            sha256_hash.update(K_d.to_bytes(2,"big"))
            hash_hex = sha256_hash.hexdigest()
            key = bytes.fromhex(hash_hex)
    
            while True:
                data  = input()
                data_encrypted,iv = encrypt_aes (data,key)
                await websocket.send(data_encrypted)
                await websocket.send(iv)
                data_rec = await websocket.recv()
                iv = await websocket.recv()
                message_recived=decrypt_aes (data_rec,key,iv)
                print("Message recived from Bob = ", message_recived.decode("utf-8"))
                await asyncio.sleep(5)


        
asyncio.get_event_loop().run_until_complete(hello())