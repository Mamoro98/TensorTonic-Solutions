from collections import Counter
import numpy as np

def mean_median_mode(x: list) -> dict:
    """
    Returns a dictionary with mean, median, and mode.
    """
    mean = np.mean(x)
    median = np.median(x)
    unique, counts = np.unique(x, return_counts = True)
    mode = unique[np.argmax(counts)]

    return {
        "mean" : float(mean),
        "median": float(median),
        "mode": float(mode)
    }
        