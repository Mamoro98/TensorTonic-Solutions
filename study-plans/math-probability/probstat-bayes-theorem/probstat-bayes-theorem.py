def bayes_theorem(p_a: float, p_b_given_a: float, p_b_given_not_a: float) -> float:
    """
    Returns the posterior probability rounded to four decimals.
    """
    p_a_not = 1-p_a
    p_b = (p_b_given_a * p_a) + (p_b_given_not_a * p_a_not)
    p_a_given_b = (p_b_given_a * p_a) / p_b
    
    return round(p_a_given_b,4)