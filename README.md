# Entropy
Entropy of encrypted data

**This project is WIP!**

##### *Disclaimer: Documentations in this project are partially written with the help of GPT.*

## Introduction
This is the final project for the course, "Math Methods for Physicists" in National Tsing Hua University. The goal of this project is to study the entropy of encrypted data. 

In followings, I will introduce some basics concepts I will use in this project.

---

<details>
<summary>Details about Information and Entropy</summary>

### Information

[Information](https://en.wikipedia.org/wiki/Information) is a measure of the uncertainty of an outcome. It is related to the amount of data that is required to specify the outcome of an event. The more uncertain an outcome is, the more information is required to resolve uncertainty of the outcome.

The information is calculated using the [Shannon information](https://en.wikipedia.org/wiki/Information_(measure)). Shannon information is defined as:

<div align="center"><img style="background: white;" src=".github/svg/Do9eHEQh4T.svg"></div>

where $p(x_i)$ is the probability of the $i$-th symbol in the data.

### Entropy

Entropy is a fundamental concept in information theory that quantifies the uncertainty or randomness associated with a random variable. It measures the average amount of information required to describe or encode an event or a set of outcomes.

The entropy is calculated using the [Shannon entropy](https://en.wikipedia.org/wiki/Entropy_(information_theory)). Shannon entropy is defined as:

<div align="center"><img style="background: white;" src=".github/svg/XrVbG3suFo.svg"></div>

where $p(x_i)$ is the probability of the $i$-th symbol in the data.

### Mutual Information

[Mutual information](https://en.wikipedia.org/wiki/Mutual_information) is a fundamental concept in information theory and statistics that measures the amount of information that two random variables share. It provides a quantitative measure of the dependence or association between the variables, revealing how much knowing the value of one variable can reduce uncertainty about the other.

The mutual information is calculated using the [Kullback-Leibler divergence](https://en.wikipedia.org/wiki/Kullback%E2%80%93Leibler_divergence). Kullback-Leibler divergence is defined as:

<div align="center"><img style="background: white;" src=".github/svg/XUJQ24fqN2.svg"></div>

where $p(x_i)$ is the probability of the $i$-th symbol in the data, and $q(x_i)$ is the probability of the $i$-th symbol in the encrypted data.

And the mutual information is defined as:

<div align="center"><img style="background: white;" src=".github/svg/l2qjm7JQsY.svg"></div>

where $P(X,Y)$ is the joint probability of $X$ and $Y$, and $P(X)P(Y)$ is the product of the marginal probabilities of $X$ and $Y$.

### Conditional Entropy

[Conditional entropy](https://en.wikipedia.org/wiki/Conditional_entropy) is a measure of the amount of information needed to describe the outcome of a random variable $Y$ given that the value of another random variable $X$ is known. It is also known as the equivocation of $Y$ given $X$.

The conditional entropy is defined as:

<div align="center"><img style="background: white;" src=".github/svg/dkBXaJHN8y.svg"></div>

where $p(x_i)$ is the probability of the $i$-th symbol in the data, and $p(y_j|x_i)$ is the probability of the $j$-th symbol in the encrypted data given the $i$-th symbol in the data.

</details>

### 1. Relation between Entropy, Mutual Information, and Conditional Entropy

There is a relation between entropy, mutual information, and conditional entropy:

$$
I(X;Y) = H(X) - H(X|Y) = H(Y) - H(Y|X)
$$

### 2. Encryption

There are three elements in encryption: plaintext, ciphertext, and key. Plaintext is the original message. Ciphertext is the encrypted message. Key is the secret used to encrypt the plaintext. The encryption process is a function that maps the plaintext and key to the ciphertext. The decryption process is a function that maps the ciphertext and key to the plaintext.

Firstly, we consider the single-bit encryption. To make sure that once we know the ciphertext and the key, we can recover the plaintext, the encryption function must be a bijection. The possible encryption functions are:

$$
f_1(0,0) = 0, f_1(0,1) = 1, f_1(1,0) = 1, f_1(1,1) = 0
$$

$$
f_2(0,0) = 1, f_2(0,1) = 0, f_2(1,0) = 0, f_2(1,1) = 1
$$

$f_1$ is XOR encryption, and $f_2$ is XNOR encryption. They both have the characteristic that ciphertext is corresponding to both 0, 1; only once we know the key is, the plane text can be recovered. And in most of cases, we pick XOR encryption as the most basic encryption to bit-wise operation.

Before we take account into multi-bits encryption, there are two important properties of the operation of a secure cipher identified by Shannon: [confusion and diffusion](https://en.wikipedia.org/wiki/Confusion_and_diffusion). Confusion means that the relationship between the ciphertext and the key must be complex and involved. Diffusion means that the statistical structure of the plaintext must be dissipated into long-range statistics of the ciphertext.



## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
