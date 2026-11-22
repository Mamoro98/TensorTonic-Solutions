import numpy as np

def gram_schmidt(vectors: list) -> np.ndarray:
    """
    Returns a float64 array whose rows form the ordered orthonormal basis.
    """
    vectors = np.array(vectors, dtype= np.float64)

    v1 = vectors[0]
    e1 = v1/np.linalg.norm(v1)

    vectors = vectors[1:]
    temp = [e1]
    for i in range(len(vectors)):
        vx = vectors[i]
        t = np.zeros(e1.shape)
        for j in range(len(temp)):
            t = t + np.dot(vx,temp[j]) * temp[j]
        ux = vx - t
        temp.append(ux/np.linalg.norm(ux))

    return np.array(temp)