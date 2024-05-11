from helpers import is_prime ,is_primitive
import random

#implement Diffie-Hellman algorithm with q (prime number) and a(its primitive root) which are public and xa and xb as private keys
#of every user are entered as inputs
#and calculate the shared key between the users
def DH(q,a):
    x_a = random.randint(1, q-1)
    y1 = (a**x_a) % q
    return x_a,y1