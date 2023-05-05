'''XOR encryption and decryption functions.'''

def xor_encrypt(message: str, key: str)-> str:
    'Encrypts a message using XOR encryption with a given key.'
    ciphertext = ""
    for i in range(len(message)):
        ciphertext += chr(ord(message[i]) ^ ord(key[i % len(key)]))
    return ciphertext

def xor_decrypt(ciphertext: str, key: str)-> str:
    'Decrypts a ciphertext using XOR encryption with a given key.'
    message = ""
    for i in range(len(ciphertext)):
        message += chr(ord(ciphertext[i]) ^ ord(key[i % len(key)]))
    return message
