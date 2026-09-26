import numpy as np

def skewness_kurtosis(data: list) -> dict:
    """
    Returns adjusted statistics and their interpretations in a dictionary.
    """
    mean = np.mean(data)
    print(f"mean is {mean}")
    n = len(data)
    print(f"n is {n}")
    total = 0
    for xi in data:
        total += ( (xi - mean) ** 2)
    s = total / (n - 1)
    s = s ** 0.5
    print(f"s is {s}")

    total = 0
    for xi in data:
        total += (( (xi - mean) / s ) ** 3)

    g1 = (n * total) / ( (n-1)*(n-2) )

    total = 0
    for xi in data:
        total += ( (xi-mean)/s ) ** 4

    g2 = ( n * (n+1) * total) / ( (n-1) * (n-2) * (n-3) )

    g2 = g2 - ( 3 * ( (n-1) ** 2)  ) / ((n-2)*(n-3)) 

    g1 = round(g1,4)
    g2 = round(g2,4)

    if g1 > 0.5:
        g1_verdict = "right-skewed"
    elif g1 < -0.5:
        g1_verdict = "left-skewed"
    else:
        g1_verdict = "approximately symmetric"

    if g2 > 1:
        g2_verdict = "leptokurtic"
    elif g2 < -1:
        g2_verdict = "platykurtic"
    else:
        g2_verdict = "mesokurtic"


    return  {"skewness": g1, "kurtosis": g2, "skew_interpretation": g1_verdict, "kurtosis_interpretation": g2_verdict}
    
    