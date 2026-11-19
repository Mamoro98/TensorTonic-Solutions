import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transposed matrix as a NumPy array.
    """
    # Write code here
    A = np.array(A)
    AT = np.zeros((A.shape[1],A.shape[0]))
    j = 0
    for i in range(A.shape[0]):
        AT[:,j] = A[i]
        j += 1

    return AT
