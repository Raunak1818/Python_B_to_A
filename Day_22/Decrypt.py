import random
import string


chars = " " + string.whitespace + string.punctuation + string.digits + string.ascii_letters
# print(chars)
chars = list(chars)
key = chars.copy()

random.shuffle(key)

# print(f"chars: {chars}")
# print(f"key : {key}")


# DECRYPT

cipher_text = input("Enter a message to encrypt: ")
plain_text = "" 

for letter in cipher_text:
    index = key.index(letter)
    # print(index)
    plain_text += chars[index]
    # print(plain_text,end="")


print(f"Encrypted message: {cipher_text}")
