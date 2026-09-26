def conditional_probability(p_a: float, p_b: float, p_a_and_b: float) -> list:
    """
    Returns both rounded conditional probabilities in the required order.
    """
    a_b = p_a_and_b / p_b
    b_a = p_a_and_b / p_a
    a_b = round(a_b,4)
    b_a = round(b_a,4)
    return [a_b,b_a]