def basis_get(data) -> list:
    "Get the basis of the data."

    basis_dict = []
    for char in data:
        if char not in basis_dict:
            basis_dict.append(char)
    return basis_dict