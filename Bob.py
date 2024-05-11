import websockets
import random
import asyncio
from DH import DH
from Elgamal import elgamalEncryption,elgamalgeneration,generateKey,elgamalEncryption, elgamalDecryption
import hashlib
from helpers import encrypt_aes, decrypt_aes
import aioconsole


async def client_send(websocket, key):
    while True:
        # data = ""
        data  = await aioconsole.ainput("")
        #encryption of the message before sending i using AES encryption algorthim
        data_encrypted,iv = encrypt_aes (data,key)

        #sending the message encrypted
        await websocket.send(data_encrypted) 
        #sending the iv
        await websocket.send(iv)


async def client_recieve(websocket, key):
    while True:
        data_rec = await websocket.recv()
        iv = await websocket.recv()
        print("Message recived from my opponent before decryption = ", data_rec)
        message_recived=decrypt_aes (data_rec,key,iv)
        print("Message recived from my opponent after decryption = ", message_recived.decode())

async def hello():
    file_path = 'public.txt'
    data_dict = {}
    #Reading the alpha and q of diffie helman and elgamal
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
    print("q of diffieHelman = ",q_d)
    print("apha of diffieHelman = ",a_d)
    print("q of ElGamal = ",q_g)
    print("alpha of ElGamal = ",a_g)

    #Generateing public and private keys using diffie helman
    x_a_d,y_a_d = DH(q_d,a_d)
    print("public key of diffieHelman = ",x_a_d)
    print("private key of diffieHelman = ",y_a_d)

    async with websockets.connect("ws://localhost:8765") as websocket:
            
            #Generatig keys using ElGamal 
            # await websocket.send("initilization")
            y_b_g = await websocket.recv()
            y_a_g , X_a_g = elgamalgeneration(q_g, a_g)
            print("public key of ElGamal = ",y_a_g)
            print("private key of ElGamal = ",X_a_g)

            #sending public key of ElGamal
            await websocket.send(str(y_a_g))

            #Reciving the public key of my opponent 
            
            print("public key of ElGamal of my opponent recieved = ",y_b_g)

            #Generate key for ElGamal
            k= generateKey(q_g)
            print("the key generated for the Signiture verfictaion = ",k)
            C1,C2 = elgamalEncryption(y_a_d, a_g, X_a_g, q_g, k)
            print("C1 generated for the Signiture verfictaion = ",C1)
            print("C2 generated for the Signiture verfictaion = ",C2)

            print("The public key is sent to my opponent")
            await websocket.send((str(y_a_d),"/",str(C1),"/",str(C2)))

            message = await websocket.recv()
            y_b_d,C1,C2 = message.split("/")
            print("C1 Recived for the Signiture verfictaion = ",C1)
            print("C2 Recived for the Signiture verfictaion = ",C2)
            print("The public key is recived from my opponent = " , y_b_d)

            v1,v2 = elgamalDecryption(y_b_d, int(C1), int(C2), int(q_g) , a_g, int(y_b_g))

            if (v1!=v2):
                print("V1 = ",v1)
                print("V2 = ",v2)
                print("The Signiture is not verifed , i wll terminate the connection")
                await websocket.close()
                return
            else:
               print("V1 = ",v1)
               print("V2 = ",v2)
               print("The Signiture is verifed")      

            K_d = ( int(y_b_d) ** x_a_d ) % q_d
            print("Aes Key before hashing = ",K_d)
            sha256_hash = hashlib.sha256()
            sha256_hash.update(K_d.to_bytes(2,"big"))
            hash_hex = sha256_hash.hexdigest()
            key = bytes.fromhex(hash_hex)
            print("Aes Key after hashing = ",key)
    
            await asyncio.gather(asyncio.create_task(client_send(websocket,key)), asyncio.create_task(client_recieve( websocket,key)))
                # await asyncio.sleep(5)


        
asyncio.get_event_loop().run_until_complete(hello())