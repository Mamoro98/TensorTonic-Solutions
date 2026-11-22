import numpy as np

def low_rank_approximation(A: list, r: int) -> np.ndarray:
    """
    Returns the best rank-r float64 approximation.
    """
    A = np.array(A, dtype= np.float64)

    U, S, V = np.linalg.svd(A)
    U = U[:,:r]
    S = np.diag(S)[:r,:r]
    V = V[:r,:]
    print(U.shape)
    print(S.shape)
    print(V.shape)

    return U @ S @ V
    