import numpy as np

def percentiles(x: list, q: list) -> np.ndarray:
    """
    Returns the requested percentiles as a float64 array.
    """
    result = []
    x = sorted(x)
    for qi in q:
        r = (qi * (len(x)-1) ) / 100
        k = np.floor(r)
        k = int(k)
        f = r - k
        if len(x) <= (k+1):
            _ = x[k]
        else:
            _ = x[k] + (f * ( x[k+1] - x[k] ) )
        result.append(_)

    return np.array(result, dtype=np.float64)
        