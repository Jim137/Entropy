import numpy as np
from typing import Union


def _basis_get(data) -> list:
    "Get the basis of the data."

    basis_dict = []
    for char in data:
        if char not in basis_dict:
            basis_dict.append(char)
    return basis_dict


def entropy(
    data: Union[str, bytes, set, list, tuple],
    base=2,
    basis_dict: Union[set, list, tuple, None] = None,
) -> float:
    """
    Return the entropy of given data.

    Parameters
    ----------
    data:   str, bytes, or iterable
    base:   int
            The logarithmic base to use, default is 2.
    basis_dict: list
                The basis of the entropy, default is None. If None, the basis will be the unique elements in data.

    Returns
    -------
    entropy:    float
                The entropy of given data.
    """

    if type(data) is bytes:
        data = list(data)
    elif type(data) is not str:
        data = str(data)

    if basis_dict is None:
        basis_dict = _basis_get(data)

    prob_list = []
    for item in basis_dict:
        prob_list.append(data.count(item) / len(data))
    entropy = 0
    for prob in prob_list:
        entropy -= prob * np.log(prob) / np.log(base)
    return entropy


if __name__ == "__main__":
    data = b"Hello World!"
    print(entropy(data))
