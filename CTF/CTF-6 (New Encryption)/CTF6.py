import string


enc = ''

with open('cipher.txt', 'r') as file:
    # Read the entire contents of the file into a string
    enc = file.read()

START = ord("a")
CHARSET = string.ascii_lowercase[:16]

def decode_b16(plain):
	decoded = ""
	for c in range(0,len(plain),2):
		first_char =  (ord(plain[c])-START)%len(CHARSET)
		sec_char = (ord(plain[c+1])-START)%len(CHARSET)

		binary_first_char = "{0:04b}".format(first_char)
		binary_sec_char = "{0:04b}".format(sec_char)
		char_ascii=int(binary_first_char+binary_sec_char, 2)

		decoded += chr(char_ascii)
		
	return decoded


def caesar_shift_decrypt(c, k):
	return CHARSET[(ord(c) - ord(k)) % len(CHARSET)] 
		 
b16=""
key = "e"

for i, c in enumerate(enc):
	b16 += caesar_shift_decrypt(c, key[i % len(key)])

decrypted = decode_b16(b16)
	
print(decrypted)