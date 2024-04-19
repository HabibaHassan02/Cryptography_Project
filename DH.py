import math

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

#implement Diffie-Hellman algorithm with q (prime number) and a(its primitive root) which are public and xa and xb as private keys
#of every user are entered as inputs
#and calculate the shared key between the users
def DH(q,a,xa,xb):
    y1 = (a**xa) % q
    y2 = (a**xb) % q
    k1 = (y2**xa) % q
    k2 = (y1 ** xb) % q

    if k1==k2:
        print("keys are shared correctly")
        print(f"K={k1}")
    else:
        print("error occured during the key sharing!")

while True:
    q= int(input("enter q which is the prime number: "))
    if is_prime(q) == False:
        print("Error! Please enter a prime number") 
        continue
    break

while True:
    a= int(input("enter a which is the primitive root of the entered prime number: "))
    if is_primitive(a,q) == False:
        print(f"Error! Please enter a primitive root number of {q}") 
        continue
    break

while True:
    xa= int(input("enter xa which is the private key of user1: "))
    xb= int(input("enter xb which is the private key of user2: "))
    if xa>q or xb>q:
        print(f"Error! Please enter private keys less than the entered prime number {q}") 
        continue
    break

DH(q,a,xa,xb)