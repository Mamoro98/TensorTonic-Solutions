import numpy as np

def mean_median_mode(x: list) -> dict:
    """
    Returns mean, median, and mode as Python floats in a dictionary.
    """
    lis, items = np.unique( x , return_counts=True)
    argma=np.argmax(items)
    mode = lis[argma]
    
    return {
        "mean": np.mean(x),
        "median": np.quantile(x, 0.5),
        "mode": float(mode)
    }