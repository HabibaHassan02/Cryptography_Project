from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

#function to check if the number is prime or not
def is_prime(num):
    if num<= 1:
        return False
    else:
        for i in range(2,num):
            if num % i == 0:
                return False
        return True

#to check if "a" is a primitive root to prime number "p" or not
def is_primitive(a,p):
    ls=[]
    for i in range(1,p):
        ls.append((a**i)%p)
    # loop over the list of powers of "a" modulo "p" to check if all values are available from 1 to p-1 and are distinct (their count is 1)
    for i in range(1,p):
        if ls.count(i) > 1:
            return False
        return True
def encrypt_aes(data, key):
    cipher = AES.new(key, AES.MODE_CBC)
    cipher_text = cipher.encrypt(pad(data, AES.block_size))
    iv = cipher.iv

    return cipher_text , iv

def decrypt_aes(cipher_text, key,iv):
    decrypt_cipher = AES.new(key, AES.MODE_CBC, iv)
    plain_text = decrypt_cipher.decrypt(cipher_text)    
    return plain_text
