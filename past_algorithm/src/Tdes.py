'''Triple DES encryption and decryption'''
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import base64


def Tdes_encrypt(key: str, plaintext: str) -> bytes:
    'Encrypts a plaintext using Triple DES encryption with a given key.'
    key = key.encode()
    plaintext = plaintext.encode()

    if len(plaintext) % 8 != 0:
        plaintext += b'\0' * (8 - len(plaintext) % 8)

    backend = default_backend()
    cipher = Cipher(algorithms.TripleDES(key), modes.ECB(), backend=backend)

    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(plaintext) + encryptor.finalize()

    return ciphertext


def Tdes_decrypt(key: str, ciphertext: bytes) -> str:
    'Decrypts a ciphertext using Triple DES encryption with a given key.'
    key = key.encode()

    backend = default_backend()
    cipher = Cipher(algorithms.TripleDES(key), modes.ECB(), backend=backend)

    decryptor = cipher.decryptor()
    plaintext = decryptor.update(ciphertext) + decryptor.finalize()

    return plaintext.rstrip(b'\0').decode()


if __name__ == "__main__":
    ciphertext = Tdes_encrypt('111111111111111111111111', 'hello world')
    print(ciphertext)
    print(str(base64.b64encode(ciphertext), 'utf-8'))
    print(Tdes_decrypt('111111111111111111111111', ciphertext))
