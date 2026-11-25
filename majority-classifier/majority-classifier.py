import numpy as np

def majority_classifier(y_train: list, X_test: list) -> np.ndarray:
    """
    Returns a one-dimensional NumPy array.
    """
    # Write code here
    d = {}
    for i in y_train:
        if i in d.keys():
            d[i] = d[i] + 1
        else:
            d[i] = 1

    max_count = 0
    max_item = None
    for key, value in d.items():
        if value > max_count:
            max_count = value
            max_item = key
        
    
        
        
    return np.zeros(np.array(X_test).shape) + max_item 