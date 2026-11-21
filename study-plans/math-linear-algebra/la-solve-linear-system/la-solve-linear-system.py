import numpy as np

def solve_linear_system(A: list, b: list) -> np.ndarray:
    """
    Returns the float64 solution vector.
    """
    return np.linalg.solve(np.array(A),np.array(b))