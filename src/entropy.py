import numpy as np


def entropy(data: bytes, base=2) -> float:
    'Computes entropy of data.'

    data_list = []
    for char in data:
        if char not in data_list:
            data_list.append(char)
    prob_list = []
    for item in data_list:
        prob_list.append(data.count(item) / len(data))
    entropy = 0
    for prob in prob_list:
        entropy -= prob * np.log(prob) / np.log(base)
    return entropy


if __name__ == '__main__':
    data = b"Hello World!"
    print(entropy(data))
