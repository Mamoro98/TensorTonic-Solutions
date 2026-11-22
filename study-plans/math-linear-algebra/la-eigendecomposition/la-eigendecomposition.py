import numpy as np

def eigendecompose(A: list) -> dict:
    """
    Returns sorted float64 eigenvalues and eigenvectors in a dictionary.
    """
    A = np.array(A, dtype= np.float64)

    values, vectors = np.linalg.eig(A)
    return {"eigenvalues": values, "eigenvectors": vectors}