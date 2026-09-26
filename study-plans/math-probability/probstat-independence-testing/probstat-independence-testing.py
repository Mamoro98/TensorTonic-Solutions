def independence_test(p_a: float, p_b: float, p_a_and_b: float) -> dict:
    """
    Returns the rounded product and independence decision in a dictionary.
    """
    test = p_a * p_b
    is_independent = round(test,4) == round(p_a_and_b,4)
    return  {"p_a_times_p_b": test, "is_independent": is_independent}