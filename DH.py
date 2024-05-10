from helpers import is_prime ,is_primitive
import random

#implement Diffie-Hellman algorithm with q (prime number) and a(its primitive root) which are public and xa and xb as private keys
#of every user are entered as inputs
#and calculate the shared key between the users
def DH(q,a):
    x_a = random.randint(1, q)
    y1 = (a**x_a) % q
    return x_a,y1

# # if k1==k2:
# #     print("keys are shared correctly")
# #     print(f"K={k1}")
# # else:
# #     print("error occured during the key sharing!")

# while True:
#     q= int(input("enter q which is the prime number: "))
#     if is_prime(q) == False:
#         print("Error! Please enter a prime number") 
#         continue
#     break

# while True:
#     a= int(input("enter a which is the primitive root of the entered prime number: "))
#     if is_primitive(a,q) == False:
#         print(f"Error! Please enter a primitive root number of {q}") 
#         continue
#     break

# while True:
#     xa= int(input("enter xa which is the private key of user1: "))
#     xb= int(input("enter xb which is the private key of user2: "))
#     if xa>q or xb>q:
#         print(f"Error! Please enter private keys less than the entered prime number {q}") 
#         continue
#     break
