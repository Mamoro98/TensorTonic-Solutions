import numpy as np

def matrix_inverse(A: list) -> np.ndarray | None:
    """
    Returns the inverse as a NumPy array, or None.
    """
    # Write code here
    try :
        inverse = np.linalg.inv(np.array(A, dtype=np.float64))
        return inverse
    except:
        return None
     