import numpy as np

def bernoulli_pmf_and_moments(x: list, p: float) -> dict:
    """
    Returns a dictionary with pmf, mean, and variance.
    """
    pmf = []
    mean = p
    variance = p * (1-p)

    for i in x:
        res = (p**i)*((1-p)**(1-i)) 
        pmf.append(res)
    return {
        "pmf":np.array(pmf),
        "mean":float(mean),
        "variance":float(variance)
    }
        