def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

def perms_and_combs(n: int, r: int) -> list:
    """
    Returns permutations, combinations, and n factorial as integers.
    """
    ordered = factorial(n) // (factorial(n-r))
    unordered = factorial(n) // (factorial(r) * factorial(n-r))
    return [ordered,unordered,factorial(n)]