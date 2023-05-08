# Cryptography
##### *Disclaimer: This is written with the help of GPT.*

Cryptography is the practice of securing communication from third-party intruders by transforming the message into an unintelligible form. It involves techniques for encrypting and decrypting messages in such a way that only the intended recipient can read the original message.

Contents:
* [XOR Encryption](#xor-encryption)
* [DES](#data-encryption-standard-des)
* [RSA](#rsa)

## Encryption

<details><summary>Brief intro to encryption</summary>

Encryption is the process of converting plain text into a coded message that is unreadable by anyone except the intended recipient. The process involves using an algorithm and a key to transform the original message into a ciphertext. There are two main types of encryption:

### Symmetric Encryption
In symmetric encryption, the same key is used for both encryption and decryption. The key is shared between the sender and the recipient, and it must be kept secret from anyone else. Examples of symmetric encryption algorithms include Advanced Encryption Standard (AES), Data Encryption Standard (DES), and Triple DES.

### Asymmetric Encryption
In asymmetric encryption, two different keys are used for encryption and decryption. The public key is used for encrypting the message, while the private key is used for decrypting the message. The public key is shared with anyone who wants to send a message, while the private key is kept secret by the recipient. Examples of asymmetric encryption algorithms include RSA and Elliptic Curve Cryptography (ECC).

### Hashing
Hashing is the process of converting a message or data into a fixed-length value, known as a hash value or digest. Hash functions are one-way functions, meaning that it is easy to compute the hash value from the original message, but it is virtually impossible to derive the original message from the hash value. Hashing is used to verify the integrity of data and to ensure that it has not been tampered with.

### Digital Signatures
A digital signature is a mathematical technique used to ensure the authenticity and integrity of a message or document. It involves using a private key to sign the message or document, which creates a unique digital signature. The digital signature can be verified using the corresponding public key to ensure that the message has not been tampered with and that it was indeed sent by the intended sender.

### Applications of Cryptography
Cryptography is used in many applications, including:

* Secure communication between two parties over an insecure network
* Secure storage of sensitive data
* Digital signatures for electronic transactions and contracts
* Password storage and verification
* Secure online banking and e-commerce transactions
* Protection of intellectual property and trade secrets

In summary, cryptography plays a crucial role in securing communication and protecting sensitive data in the digital age.

</details>

---

*In the followings, we will discuss some of the most common encryption algorithms and what we will be using in this project as examples.*

## XOR Encryption

XOR (exclusive or) encryption is a type of symmetric encryption that involves bitwise operations on binary data. It works by combining a plaintext message with a secret key using the XOR operation, which produces a ciphertext. The same key is used for both encryption and decryption.


<div align="center">
    <img src="../.github/xor.svg" width="300" height="300" alt="XOR true table">
</div>

### How it works
XOR encryption works by comparing each bit in the plaintext message with the corresponding bit in the secret key. If the bits are the same, the resulting bit in the ciphertext is 0. If the bits are different, the resulting bit in the ciphertext is 1. This process is repeated for each bit in the message, producing a ciphertext that is the same length as the plaintext.

The key used for encryption must be kept secret from anyone who should not have access to the encrypted message. If the key is known, it is relatively easy to decrypt the message by applying the same XOR operation with the key to the ciphertext.

### Advantages and disadvantages
XOR encryption has some advantages and disadvantages:

**Advantages**

* Simple and fast to implement.
* Can be used for both encryption and decryption.
* Ciphertext appears random, making it difficult to decipher without the key.
  
**Disadvantages**

* Vulnerable to known plaintext attacks, where an attacker can use knowledge of the plaintext to derive the key.
* Vulnerable to brute-force attacks, where an attacker tries every possible key until the correct one is found.
* Does not provide strong security compared to modern encryption algorithms.

### Example Code
```python
def xor_encrypt(message, key):
    ciphertext = ""
    for i in range(len(message)):
        ciphertext += chr(ord(message[i]) ^ ord(key[i % len(key)]))
    return ciphertext

def xor_decrypt(ciphertext, key):
    message = ""
    for i in range(len(ciphertext)):
        message += chr(ord(ciphertext[i]) ^ ord(key[i % len(key)]))
    return message
```

### Conclusion
XOR encryption is a simple and fast method of symmetric encryption, but it is not as secure as modern encryption algorithms. It is vulnerable to known plaintext attacks and brute-force attacks, making it unsuitable for many applications that require strong security. However, it can be useful for simple tasks where security is not a major concern.

## Data Encryption Standard (DES)
The Data Encryption Standard (DES) is a symmetric key encryption algorithm that was developed in the 1970s by IBM and adopted by the US government as a standard for encrypting sensitive data. It is a block cipher that encrypts data in 64-bit blocks using a 56-bit key.

### How it works
DES works by dividing the plaintext message into 64-bit blocks and applying a series of mathematical operations to each block to produce the ciphertext. The same key is used for both encryption and decryption.

#### Key Generation
To generate the key, a 64-bit key is input to a key generation algorithm that produces 16 subkeys, each of which is 48 bits long. These subkeys are used in the encryption and decryption processes.

#### Encryption
The encryption process consists of 16 rounds, each of which uses a different subkey. Each round takes a 64-bit block of plaintext and produces a 64-bit block of ciphertext.

1. Initial permutation: The plaintext block is permuted according to a fixed permutation table.
2. Key mixing: The 64-bit block is divided into two 32-bit halves, and the right half is expanded to 48 bits using a fixed expansion table. The 48-bit result is XORed with the current subkey.
3. Substitution: The 48-bit result is divided into eight 6-bit blocks, each of which is substituted using a different 8x6-bit substitution table (S-box). The result is a 32-bit block.
4. Permutation: The 32-bit block is permuted according to a fixed permutation table.
5. Swap: The left and right halves of the block are swapped.
6. Repeat steps 2-5 for 15 more rounds, using a different subkey for each round.
7. Final permutation: The resulting 64-bit block is permuted according to a fixed permutation table to produce the ciphertext block.

#### Decryption
The decryption process is the reverse of the encryption process. The ciphertext block is input, and the subkeys are used in reverse order to produce the plaintext block.

1. Initial permutation: The ciphertext block is permuted according to a fixed permutation table.
2. Key mixing: The 64-bit block is divided into two 32-bit halves, and the right half is expanded to 48 bits using a fixed expansion table. The 48-bit result is XORed with the last subkey.
3. Substitution: The 48-bit result is divided into eight 6-bit blocks, each of which is substituted using a different 8x6-bit substitution table (S-box), in reverse order. The result is a 32-bit block.
4. Permutation: The 32-bit block is permuted according to a fixed permutation table.
5. Swap: The left and right halves of the block are swapped.
6. Repeat steps 2-5 for 15 more rounds, using the subkeys in reverse order.
7. Final permutation: The resulting 64-bit block is permuted according to a fixed permutation table to produce the plaintext block.

### Advantages and disadvantages
DES has some advantages and disadvantages:

#### Advantages
* Widely used and well-studied.
* Relatively fast and efficient for its time.
* Provides a reasonable level of security against attacks, especially with longer keys.
  
#### Disadvantages
* Vulnerable to brute-force attacks, where an attacker tries every possible key until the correct one is found.
* Uses a relatively short key, making it vulnerable to attacks using specialized hardware.
* Has been replaced by more secure encryption algorithms, such as AES.

### Conclusion
DES is a well-known and widely used encryption algorithm that has been widely used for decades. However, due to its relatively short key length and vulnerability to brute-force attacks, it has been gradually replaced by newer and more secure encryption algorithms.

In 1997, a machine was built that was able to brute-force a DES key in under a day, highlighting the need for stronger encryption methods. In response, the US government began promoting the use of Triple DES (3DES), which uses three iterations of DES with different keys to provide greater security.

Today, DES is considered an obsolete encryption algorithm and is not recommended for use in new systems. However, it remains important for historical and educational purposes, as well as in legacy systems that have not yet been upgraded to more modern encryption methods.

## RSA
RSA (Rivest-Shamir-Adleman) is an asymmetric encryption algorithm widely used for secure communication, digital signatures, and key exchange. It was introduced in 1977 by Ron Rivest, Adi Shamir, and Leonard Adleman. RSA relies on the mathematical properties of prime numbers and modular arithmetic.

### Key Generation
RSA encryption involves generating a public key and a private key pair:

1. Select two distinct prime numbers, p and q.
2. Calculate the modulus, n, by multiplying p and q: n = p * q.
3. Compute the totient function, φ(n), which represents the number of positive integers less than n that are coprime (having no common factors) with n: φ(n) = (p-1) * (q-1).
4. Choose an integer, e, such that 1 < e < φ(n) and e is coprime with φ(n). This is the public exponent.
5. Calculate the modular multiplicative inverse of e modulo φ(n) to find d, the private exponent: d ≡ e^(-1) (mod φ(n)).
6. The public key consists of the modulus, n, and the public exponent, e.
7. The private key consists of the modulus, n, and the private exponent, d.

### Encryption
To encrypt a message using RSA:

1. Obtain the recipient's public key (modulus, n, and public exponent, e).
2. Represent the message as an integer m, where m < n.
3. Calculate the ciphertext, c, by computing c ≡ m^e (mod n).
4. Transmit the ciphertext to the recipient.

### Decryption
To decrypt the ciphertext using RSA:

1. Obtain the recipient's private key (modulus, n, and private exponent, d).
2. Retrieve the ciphertext, c.
3. Calculate the original message, m, by computing m ≡ c^d (mod n).

### Security
The security of RSA is based on the difficulty of factoring large integers into prime factors. The strength of RSA depends on the length of the key, typically measured in bits. A longer key size provides greater security but requires more computational resources.

RSA is susceptible to attacks if the keys are not generated properly or if an attacker discovers a more efficient factoring algorithm. Thus, it is essential to use sufficiently large key sizes and follow best practices for key generation.

### Applications
RSA has various applications, including:

* Secure communication: RSA encryption is used to establish secure channels for transmitting sensitive information over untrusted networks.
* Digital signatures: RSA can generate and verify digital signatures, ensuring the authenticity and integrity of digital documents.
* Key exchange: RSA allows two parties to securely exchange symmetric encryption keys, enabling secure communication using a faster symmetric algorithm.
* Secure sockets layer (SSL) and transport layer security (TLS): RSA is used for secure web browsing and secure email communication.

In summary, RSA is a widely adopted asymmetric encryption algorithm used for secure communication, digital signatures, and key exchange. It relies on the mathematical properties of prime numbers and modular arithmetic to provide security in various applications.