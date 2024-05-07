# Open the file in binary mode
with open('C:/Users/Habiba ElHussieny/Downloads/Computer Security/Project/Cryptography_Project/CTF/CTF-4 (Bit Shifting)/bits.txt', 'rb') as f:
    # Read the entire file as binary data
    binary_data = f.read()

# Convert binary data to a string of 0s and 1s
binary_string = ''.join(format(byte, '08b') for byte in binary_data)

# Print or use the binary string
# print(binary_string)
# print('----------------------')

def binary_to_text(binary_string):
    # Convert binary string to ASCII code then to ASCII characters
    text = ''.join(chr(int(binary_string[i:i+8], 2)) for i in range(0, len(binary_string), 8))
    return text

def shift_bits(binary_string, shift):
    # Shift the binary string
    shifted_binary = binary_string[shift:] + binary_string[:shift]
    return shifted_binary


# Iterate through different shift values
# for shift in range(1,50):

#I iterated by different shift values and found that the most readable one was the shift by 1 

# Shift the bits
shifted_binary = shift_bits(binary_string, 1)
# print(shifted_binary)

# # Convert shifted binary to text
shifted_text = binary_to_text(shifted_binary)
# print("------------------------------------------")

# # Print the result
print("Text:", shifted_text)

"""Text: Hello and welcome to file11 forensic challenge. This is just filler text to make it longer.

fastctf{a_bit_tricky|"""

