import numpy as np

def sample_var_std(x: list) -> dict:
    """
    Returns sample variance and standard deviation as Python floats.
    """
    mean = np.mean(x)
    total = 0
    for i in x:
        total += (i - mean) ** 2

    variance = total / (len(x) - 1)
    std = variance ** 0.5

    return {
        "variance": variance,
        "std_dev": std
    }
    