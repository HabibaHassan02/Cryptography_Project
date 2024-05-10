import websockets
import random
import asyncio
from DH import DH
from Elgamal import elgamalEncryption,elgamalgeneration,generateKey,elgamalEncryption, elgamalDecryption
import hashlib
from helpers import encrypt_aes, decrypt_aes

async def hello():
    file_path = 'public.txt'
    with open(file_path, 'r') as file:
        i = 0
        for line in file:
            if (i == 0):
                q = line
            else:
                a = line
            i+=1

    x_a_d,y_a_d = DH(q,a)

    async with websockets.connect("ws://localhost:8765") as websocket:
            y_a_g , X_a_g = elgamalgeneration(q, a)
            await websocket.send(str(y_a_g))
            y_b_g = await websocket.recv()
            k,K = generateKey(q,int(y_b_g))
            C1,C2 = elgamalEncryption(y_a_d, a, X_a_g, q, k, K)
            await websocket.send(str(y_a_d),str(C1),str(C2))
            y_a_d,C1,C2 = await websocket.recv()
            M = elgamalDecryption(int(C1), int(C2),  int(q) , int(y_a_g))
            y_b_d = int(M)
            K_d = (y_b_d**x_a_d)%q
            sha256_hash = hashlib.sha256()
            sha256_hash.update(K_d)
            hash_hex = sha256_hash.hexdigest()
            print("hash_hex = ",hash_hex)

            while True:
                 data  = input()
                 data_encrypted,iv = encrypt_aes (data,hash_hex)
                 await websocket.send(str(data_encrypted),str(iv))
                 data_rec,iv = await websocket.recv()
                 decrypt_aes (data_rec,hash_hex,iv)
                 await asyncio.sleep(5)


        
asyncio.get_event_loop().run_until_complete(hello())