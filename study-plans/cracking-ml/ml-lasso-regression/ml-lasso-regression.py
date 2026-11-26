import numpy as np

def lasso_regression(X: list, y: list, alpha: float, lr: float, epochs: int) -> tuple:
    """
    Returns the fitted weight list and bias.
    """
    X = np.array(X, dtype= np.float64)
    y = np.array(y, dtype= np.float64)
    w = np.zeros(X.shape[1])
    b = float(0)
    n = X.shape[0]

    for i in range(epochs):
        y_dash = X @ w + b
        error  = y_dash - y
        sum_error = np.sum(error ** 2)
        sum_w = np.sum(np.abs(w))
        Loss = (1/n) * sum_error + alpha * sum_w
        dw = (2/n) * X.T @ error + alpha * np.sign(w)
        db = (2/n) * np.sum(error)
        w = w - lr * dw
        b = b - lr * db

    return (np.round(w,decimals=4), np.round(b,decimals = 4))
