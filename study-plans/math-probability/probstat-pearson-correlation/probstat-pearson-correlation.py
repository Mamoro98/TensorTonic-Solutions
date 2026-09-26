import numpy as np

def pearson_correlation(X: list) -> np.ndarray:
    """
    Returns the float64 feature-correlation matrix.
    """
    X = np.array(X)
    features = []
    n_feat = len(X[0,:])
    for i in range(n_feat):
        features.append(X[:,i])
    return np.corrcoef(features)
            
        
        

    
    