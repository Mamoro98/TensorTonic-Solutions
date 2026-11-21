import numpy as np

def matrix_vector_multiply(A: list, x: list) -> np.ndarray:
    """
    Returns the matrix-vector product as a float64 array.
    """
    A = np.array(A,dtype=float)
    y = np.zeros(A.shape[0])
    j = 0
    for i in range(A.shape[1]):
        y = y + (x[j] * A[:,i])
        j = j +  1
    
    return y