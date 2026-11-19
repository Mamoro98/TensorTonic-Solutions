import numpy as np

def manhattan_distance(x: list, y: list) -> float:
    """
    Returns the Manhattan distance as a Python float.
    """
    # Write code here
    sum = float(0)
    for _,(i,j) in enumerate(zip(x,y)):
        sum += np.abs(i-j)
    return sum