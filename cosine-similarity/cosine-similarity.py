import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    # Write code here
    norm1 = float(np.linalg.norm(a))
    norm2 = float(np.linalg.norm(b))
    if norm1 == 0 or norm2 == 0:
        return float(0)
    

    dot_result = float(np.dot(a,b))

    cosine_similarity = float(dot_result/(norm1*norm2))

    return cosine_similarity