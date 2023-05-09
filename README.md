# Entropy
Entropy of encrypted data

**This project is WIP!**

##### *Disclaimer: Documentations in this project are partially written with the help of GPT.*

## Introduction
This is the final project for the course, "Math Methods for Physicists" in National Tsing Hua University. The goal of this project is to study the entropy of encrypted data. 

In followings, I will introduce some basics concepts I will use in this project.

### Entropy

Entropy is a fundamental concept in information theory that quantifies the uncertainty or randomness associated with a random variable. It measures the average amount of information required to describe or encode an event or a set of outcomes.

The entropy is calculated using the [Shannon entropy](https://en.wikipedia.org/wiki/Entropy_(information_theory)). Shannon entropy is defined as:

$$
H(X) = -\sum_{i=1}^{n} p(x_i) \log p(x_i)
$$

where $p(x_i)$ is the probability of the $i$-th symbol in the data.

### Mutual Information

[Mutual information](https://en.wikipedia.org/wiki/Mutual_information) is a fundamental concept in information theory and statistics that measures the amount of information that two random variables share. It provides a quantitative measure of the dependence or association between the variables, revealing how much knowing the value of one variable can reduce uncertainty about the other.

The mutual information is calculated using the [Kullback-Leibler divergence](https://en.wikipedia.org/wiki/Kullback%E2%80%93Leibler_divergence). Kullback-Leibler divergence is defined as:

$$
D_{KL}(P||Q) = \sum_{i=1}^{n} p(x_i) \log \frac{p(x_i)}{q(x_i)}
$$

where $p(x_i)$ is the probability of the $i$-th symbol in the data, and $q(x_i)$ is the probability of the $i$-th symbol in the encrypted data.

And the mutual information is defined as:

$$
I(X;Y) = D_{KL}(P(X,Y)||P(X)P(Y))
$$

where $P(X,Y)$ is the joint probability of $X$ and $Y$, and $P(X)P(Y)$ is the product of the marginal probabilities of $X$ and $Y$.

### Conditional Entropy

[Conditional entropy](https://en.wikipedia.org/wiki/Conditional_entropy) is a measure of the amount of information needed to describe the outcome of a random variable $Y$ given that the value of another random variable $X$ is known. It is also known as the equivocation of $Y$ given $X$.

The conditional entropy is defined as:

$$
H(Y|X) = -\sum_{i=1}^{n} p(x_i) \sum_{j=1}^{m} p(y_j|x_i) \log p(y_j|x_i)
$$

where $p(x_i)$ is the probability of the $i$-th symbol in the data, and $p(y_j|x_i)$ is the probability of the $j$-th symbol in the encrypted data given the $i$-th symbol in the data.

### Relation between Entropy, Mutual Information, and Conditional Entropy

There is a relation between entropy, mutual information, and conditional entropy:

$$
I(X;Y) = H(X) - H(X|Y) = H(Y) - H(Y|X)
$$

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
