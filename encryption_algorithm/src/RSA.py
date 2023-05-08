from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
import base64


def key_gen(expoent: int = 65537, key_size: int = 2048):
    'Generates a public and private key pair for RSA encryption.'
    private_key = rsa.generate_private_key(
        public_exponent=expoent, key_size=key_size
    )
    public_key = private_key.public_key()
    return private_key, public_key


def public_pem(public_key):
    'Converts public key to PEM format for storage or transmission.'
    public_pem_str = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    return public_pem_str


def private_pem(private_key):
    'Converts private key to PEM format for storage or transmission.'
    private_pem_str = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )
    return private_pem_str


def RSA_encrypt(message, public_key):
    'Encrypts a message using RSA encryption.'
    ciphertext = public_key.encrypt(
        message,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return ciphertext


def RSA_decrypt(ciphertext, private_key):
    'Decrypts a message using RSA encryption.'
    decrypted_message = private_key.decrypt(
        ciphertext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return decrypted_message


if __name__ == "__main__":
    private_key, public_key = key_gen()

    public_pem_str = public_pem(public_key)
    private_pem_str = private_pem(private_key)
    print("Public key:", public_pem_str)
    print("Private key:", private_pem_str)

    message = b"Hello World!"
    ciphertext = RSA_encrypt(message, public_key)
    decrypted_message = RSA_decrypt(ciphertext, private_key)

    print("Original message:", message)
    print("Encrypted message:", str(base64.b64encode(ciphertext), 'utf-8'))
    print("Decrypted message:", decrypted_message)
