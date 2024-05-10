import random
from math import floor

def extended_ecludian (phy,r0:int,r1:int,x0:int,x1:int,y0:int,y1:int):
    
    if r1 == 1:
        return r1
    
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
    y_a = (alpha ** X_a) % q

    k = random.randint(1, q - 1)
    K = (y_a ** k) % q

    return y_a , X_a
def generateKey (q: int,Y_b_gamal):
    k = random.randint(1, q - 1)
    K = (Y_b_gamal ** k) % q
    return k,K

def elgamalEncryption(M: int, alpha:int, X_a:int, q:int, k:int, K:int):
    
    C1 = (alpha ** k) % q
    C2 = (K * M) % q 

    return C1, C2

def elgamalDecryption(C1: int, C2: int, q: int, X_a: int):
    K = (C1 ** X_a) % q
    K_inverse = extended_ecludian(q,q,K,1,0,0,1)
    M = (C2 * K_inverse) % q
    return M

