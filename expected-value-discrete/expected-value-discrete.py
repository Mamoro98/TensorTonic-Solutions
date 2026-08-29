import numpy as np

def expected_value_discrete(x: list, p: list) -> float:
    """
    Returns the expected value as a Python float.
    """
    # Write code here
    zipped = zip(x,p)
    sum = float(0)
    for idx, (item,prob) in enumerate(zipped):
        sum += (item*prob)
    return float(sum)
        