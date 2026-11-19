import numpy as np

def vector_norms(v: list) -> np.ndarray:
    """
    Returns a float64 array containing the L1, L2, and infinity norms.
    """
    Linf = max(np.abs(v))

    L1 = float(0)
    L2 = float(0)

    for i in v:
        L1 += np.abs(i)
        L2 += i ** 2

    return np.array([float(L1), float(L2 ** 0.5),float(Linf)])
    