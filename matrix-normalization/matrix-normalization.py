import numpy as np

def matrix_normalization(matrix: list, axis=None, norm_type: str = "l2") -> np.ndarray:
    """
    Returns a NumPy array with the same shape as matrix.
    """
    # Write code here
    matrix = np.array(matrix, dtype= np.float64)
    norms = []
    if axis == 1:
        if norm_type == "l1":
            for i in range(matrix.shape[0]):
                norm = np.linalg.norm(matrix[i,:],1)
                if norm == 0:
                    continue
                matrix[i,:] = matrix[i,:]/norm
            return matrix
        elif norm_type == "l2":
            for i in range(matrix.shape[0]):
                norm = np.linalg.norm(matrix[i,:],2)
                if norm==0:
                    continue
                matrix[i,:] = matrix[i,:]/norm
            return matrix
        else:
            for i in range(matrix.shape[0]):
                norm = np.linalg.norm(matrix[i,:], np.inf)
                if norm==0:
                    continue
                matrix[i,:] = matrix[i,:]/norm
            return matrix
    elif axis == 0:
        if norm_type == "l1":   
            for i in range(matrix.shape[1]):
                norm = np.linalg.norm(matrix[:,i],1)
                if norm==0:
                    continue
                matrix[:,i] = matrix[:,i]/norm
            return matrix
        elif norm_type == "l2":
            for i in range(matrix.shape[1]):
                norm = np.linalg.norm(matrix[:,i],2)
                if norm==0:
                    continue
                matrix[:,i] = matrix[:,i]/norm
            return matrix
        else:
            for i in range(matrix.shape[1]):
                norm = np.linalg.norm(matrix[:,i], np.inf)
                if norm==0:
                    continue
                matrix[:,i] = matrix[:,i]/norm
            return matrix
    else:
        if norm_type == "l1":   
            norm = np.linalg.norm(matrix.flatten(),1)
            if norm == 0:
                return matrix
            matrix = matrix/norm
            return matrix
        elif norm_type == "l2":
            norm = np.linalg.norm(matrix.flatten(),2)
            if norm==0:
                    return matrix
            matrix = matrix/norm
            return matrix
        else:
            norm = np.linalg.norm(matrix.flatten(), np.inf)
            if norm==0:
                    return matrix
            matrix = matrix/norm
            return matrix
        