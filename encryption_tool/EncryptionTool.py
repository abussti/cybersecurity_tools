import random
import string

#adding characters to a separate list for the key and the encrypted message
chars = string.ascii_letters + string.digits + string.punctuation + " "
chars = list(chars)
key = chars.copy()

#randomizing the list of chars to get an encrypted message
random.shuffle(key)

#encrypt
plain_text = input("Enter a message to encrypt: ")
encrypted_text = ""

#for every letter in the message we replace it with a dedicated random character from the key list
for letter in plain_text:
    index = chars.index(letter)
    encrypted_text += key[index]

#printing results
print(f"original message: {plain_text}")
print(f"encrypted message: {encrypted_text}")