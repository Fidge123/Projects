# **Caesar cipher** - Implement a Caesar cipher, both encoding and decoding. ...

secret = input("Enter secret message: ").upper()
key = int(input("Enter key as number: "))
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print(secret.translate(str.maketrans(alphabet, alphabet[key:] + alphabet[:key])))
