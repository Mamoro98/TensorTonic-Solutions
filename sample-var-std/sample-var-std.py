import numpy as np

def sample_var_std(x: list) -> dict:
    """
    Returns a dictionary with variance and standard_deviation.
    """
    mean = np.mean(x)
    sum = 0
    for i in x:
        sum = sum + (i-mean)**2
    s_square = sum/(len(x)-1)
    s = s_square ** (0.5)
    return {
        "variance": float(s_square),
        "standard_deviation" : float(s)
    }
        