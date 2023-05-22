import numpy as np
from typing import Union

from .utils.basis_get import basis_get


def KLD(
    dataX: Union[str, bytes, list, tuple],
    dataY: Union[str, bytes, list, tuple],
    base=2,
    basis_dict: Union[set, list, tuple, None] = None,
) -> float:
    """
    Return the Kullback-Leibler divergence of given dataX and dataY.

    Parameters
    ----------
    dataX:   str, bytes, or iterable
    dataY:   str, bytes, or iterable
    base:   int
            The logarithmic base to use, default is 2.
    basis_dict: list
                The basis of the information, default is None. If None, the basis will be the unique elements in data.

    Returns
    -------
    div:    float
            The Kullback-Leibler divergence of given dataX and dataY.
    """
    
    for data in [dataX, dataY]:
        if type(data) is bytes:
            data = list(data)
        elif type(data) is not str:
            data = str(data)

    if basis_dict is None:
        basis_dict = basis_get(dataX)

    probX = []
    probY = []
    for item in basis_dict:
        if dataY.count(item) == 0:
            return np.inf
        probX.append(dataX.count(item) / len(dataX))
        probY.append(dataY.count(item) / len(dataY))

    div = 0
    for i in range(len(probX)):
        if probX[i] == 0:
            continue
        div += probX[i] * np.log(probX[i] / probY[i]) / np.log(base)
    return div


if __name__ == "__main__":
    dataX = b"hello world"
    dataY = b"wheel rolled"
    print(KLD(dataX, dataY))
