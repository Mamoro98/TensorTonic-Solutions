import numpy as np

def svd(A: list) -> dict:
    """
    Returns a dictionary containing float64 arrays U, s, and Vt.
    """
    # A = np.array(A,dtype=np.float64)
    # M = A.T @ A
    # values, vectors = np.linalg.eigh(M)
    # values = values[::-1]
    # vectors = vectors[:,::-1].T
    # k = min(A.shape[0],A.shape[1])
    # values = values[0:k]
    # vectors = vectors[:k,:]
    # values = np.clip(values,0,None,out=values)
    # sigmas = values ** 0.5
    # temp = []
    # for v in vectors:
    #     temp.append(v/np.linalg.norm(v))
    # V = np.array(temp).T
    # temp = []
    # for i in range(len(vectors)):
    #     temp.append(A @ vectors[i] / sigmas[i])
    # U = np.array(temp).T
    # I = np.identity(len(sigmas))
    # S = sigmas 
    U,S,V =  np.linalg.svd(A, full_matrices=False)
    return {
        "U" : U,
        "s": S,
        "Vt": V
    }
        
