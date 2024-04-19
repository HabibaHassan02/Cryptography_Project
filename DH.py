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
def DH(q,a,x1,x2):
    y1 = (a**x1) % q
    y2 = (a**x2) % q
    k1 = (y2**x1) % q
    k2 = (y1 ** x2) % q

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
    x1= int(input("enter x1 which is the private key of user1: "))
    x2= int(input("enter x2 which is the private key of user2: "))
    if x1>q or x2>q:
        print(f"Error! Please enter private keys less than the entered prime number {q}") 
        continue
    break

DH(q,a,x1,x2)