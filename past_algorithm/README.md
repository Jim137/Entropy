# Cryptography
### *Disclaimer: This is written with the help of GPT.*

Cryptography is the practice of securing communication from third-party intruders by transforming the message into an unintelligible form. It involves techniques for encrypting and decrypting messages in such a way that only the intended recipient can read the original message.

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

<div class="info_block" align="center">

**&#9432;XOR true table:**
|       | 0   | 1   |
| ----- | --- | --- |
| **0** | 0   | 1   |
| **1** | 1   | 0   |

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

<!-- css style -->
<style>
    .success_block {
    padding: 15px; border: 1px solid transparent; border-color: transparent; margin-bottom: 20px; border-radius: 4px; color: #3c763d; background-color: #dff0d8; border-color: #d6e9c6;
}
    .error_block {
    padding: 15px; border: 1px solid transparent; border-color: transparent; margin-bottom: 20px; border-radius: 4px; color: #a94442; background-color: #f2dede; border-color: #ebccd1;
}
    .info_block {
    padding: 15px; border: 1px solid transparent; border-color: transparent; margin-bottom: 20px; border-radius: 4px; color: #31708f; background-color: #d9edf7; border-color: #bce8f1;
}
</style>
