import numpy as np

def mahalanobis_distance(x: list, mean: list, cov: list) -> float:
    """
    Returns the Mahalanobis distance as a Python float.
    """
    x = np.array(x,dtype = np.float64)
    mean = np.array(mean, dtype=np.float64)
    cov = np.array(cov, dtype=np.float64)

    xmean = x - mean
    temp = np.linalg.solve(cov,xmean)
    temp = xmean.T @ temp
    return temp ** 0.5