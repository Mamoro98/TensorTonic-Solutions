import numpy as np

def projection_matrix(A: list) -> np.ndarray:
    """
    Returns the float64 projector onto the column space of A.
    """
    A = np.array(A, dtype = np.float64)
    a = A.T @ A
    print(a.shape)
    print(A.T.shape)
    
    b=np.linalg.solve(a,A.T)
    return A @ b