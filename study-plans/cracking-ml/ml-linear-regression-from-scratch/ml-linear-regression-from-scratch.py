import numpy as np

def linear_regression_from_scratch(X: list, y: list, lr: float, epochs: int) -> tuple:
    """
    Returns the fitted weight list and bias.
    """
    X = np.array(X, dtype=np.float64)
    y = np.array(y, dtype=np.float64)
    w = np.zeros(X.shape[1],dtype=np.float64)
    b = np.zeros(X.shape[0],dtype=np.float64)
    n = X.shape[0]

    for i in range(epochs):
        y_dash = (X @ w) + b
        error = (y_dash - y)
        loss = (1/n) * np.sum(error**2)
        dw = (2/n) * X.T @ error
        db = (2/n) * np.sum(error)
        w = w - (lr * dw)
        b = b - (lr * db)
    return (np.round(w,decimals = 4), np.round(b[0],decimals = 4))
