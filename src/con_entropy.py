import numpy as np
from typing import Union

from .mutual_info import mutual_info
from .entropy import entropy


def con_entropy(
    dataX: Union[str, bytes, list, tuple],
    dataY: Union[str, bytes, list, tuple],
    base=2,
    basis_dict: Union[set, list, tuple, None] = None,
) -> float:
    return entropy(dataX, base, basis_dict=basis_dict) - mutual_info(dataX, dataY, base)


if __name__ == "__main__":
    dataX = b"hello world!"
    dataY = b"wheel rolled"
    print(con_entropy(dataX, dataY))
