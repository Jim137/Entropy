import numpy as np
from typing import Union
from sklearn.metrics import mutual_info_score


def mutual_info(
    dataX: Union[str, bytes, list, tuple],
    dataY: Union[str, bytes, list, tuple],
    base=2,
):
    """
    Return the mutual information of given dataX and dataY.

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
    mi:    float
            The mutual information of given dataX and dataY.

    """

    x = []
    if type(dataX) is bytes:
        x = list(dataX)
    elif type(dataX) is str:
        for char in dataX:
            x.append(char)
    else:
        x = dataX

    y = []
    if type(dataY) is bytes:
        y = list(dataY)
    elif type(dataY) is str:
        for char in dataY:
            y.append(char)
    else:
        y = dataY

    if len(x) != len(y):
        print("Error: The length of dataX and dataY should be equal.")
        raise ValueError

    mi = mutual_info_score(x, y) / np.log(base)
    return mi


if __name__ == "__main__":
    dataX = b"hello world!"
    dataY = b"wheel rolled"
    print(mutual_info(dataX, dataY))
