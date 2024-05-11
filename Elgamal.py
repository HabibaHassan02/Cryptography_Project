import random
from math import floor
import hashlib
from helpers import gcd
def extended_ecludian (phy,r0:int,r1:int,x0:int,x1:int,y0:int,y1:int):
    
    if r1 == 1 :
        return r1
    # print("r1 = ", r1)
    # if r1 == 0 :
    #     return y0 % phy
   
    r = r0 % r1
    q = floor(r0/r1)
    x = x0 - q * x1 
    y = y0 - q * y1

    if r == 1 :
        return y % phy
    else:
       return extended_ecludian (phy,r1,r,x1,x,y1,y)

def elgamalgeneration( q: int, alpha: int):

    X_a = random.randint(2, q - 2)
    y_a = pow(alpha , X_a) % q

    return y_a , X_a

def generateKey (q: int):
    k = random.randint(1, q - 1)
    while (gcd(k,q-1) != 1 ):
        k = random.randint(1, q - 1)
    return k

def elgamalEncryption(M: int, alpha:int, X_a:int, q:int, k:int):
    
    C1 = pow(alpha, k) % q
    sha1_hash = hashlib.sha1()
    sha1_hash.update(str(M).encode())
    hash_hex = sha1_hash.hexdigest()
    m =  int(hash_hex,16)
    lst_bits = 1
    while(m >= q-1):
        binary_rep =  bin(m)[2:]
        m = int(binary_rep[lst_bits:],2)

    K_inverse = extended_ecludian(q-1,q-1,k,1,0,0,1)
    #K_inverse = pow(k,-1,q-1)
    C2 = K_inverse * ((m - X_a*C1)% (q-1))
    return C1, C2 % (q-1)

def elgamalDecryption(y_b_d: int, C1: int, C2: int, q: int,a: int, y_b_g: int):
    if not (1 < C1 < q-1 and 0 < C2 < q-1):
        return 1,0
    
    sha1_hash = hashlib.sha1()
    sha1_hash.update(str(y_b_d).encode())
    hash_hex = sha1_hash.hexdigest()
    m =  int(hash_hex,16)
    lst_bits = 1
    while(m >= q-1):
        binary_rep =  bin(m)[2:]
        m = int(binary_rep[lst_bits:],2)
    print(y_b_d)
    v1 = (pow(y_b_g,C1) * pow(C1,C2)) % q
    v2 = pow(a , m) % q
    return v1,v2

