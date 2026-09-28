from math import comb

def binomial_distribution(n: int, p: float, threshold: int) -> dict:
    """
    Returns the PMF, mean, variance, and probability at least threshold.
    """
    pmf = []
    for i in range(n+1):
        c = comb(n,i)
        success = p**i
        failure = (1-p)**(n-i)
        pmf.append(round(c*success*failure,4))

    mean = round(n*p,4)
    variance = round(n*p*(1-p),4)
    prob_at_least = 0
    for i in range(threshold,n+1,1):
        prob_at_least += pmf[i]
    prob_at_least = round(prob_at_least,4)
    return  {"mean":mean,"pmf":pmf,"prob_at_least":prob_at_least,"variance":variance}