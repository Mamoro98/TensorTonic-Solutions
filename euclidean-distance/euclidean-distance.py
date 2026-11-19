import numpy as np

def euclidean_distance(x: list, y: list) -> float:
    """
    Returns the Euclidean distance as a Python float.
    """
    # Write code here
    sum_s = float(0)
    for index,(i,j) in enumerate(zip(x,y)):
        sum_s += (i-j)**2
    return sum_s ** 0.5