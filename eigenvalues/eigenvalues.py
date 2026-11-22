import numpy as np

def calculate_eigenvalues(matrix: list) -> np.ndarray:
    """
    Returns a sorted NumPy array of real eigenvalues.
    """
    # Write code here
    matrix = np.array(matrix, dtype=np.float64)
    values, vectors = np.linalg.eig(matrix)
    return np.array(sorted(values), dtype=np.float64)