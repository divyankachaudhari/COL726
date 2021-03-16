import numpy as np

def orthogonalizePolynomials(P):
    n = P.shape[1]
    for j in range(n):
        for k in range(j):
            P[:, j] -= np.dot(P[:, k], P[:, j]) * P[:, k]
        P[:, j] = P[:, j] / np.linalg.norm(P[:, j])
    return P
