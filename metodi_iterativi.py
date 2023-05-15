import numpy as np


def gauss_seidel(A, b, x0, tol, k_max):
    # dimensione del sistema
    n = len(A)

    # inizializzazione ciclo di calcolo
    x1 = np.zeros(n)
    b_norm = np.linalg.norm(b)
    k = 0
    stop = False

    # ciclo di calcolo
    while not stop and k < k_max:
        for i in range(n):
            S = 0
            for j in range(i):
                S = S + A[i, j] * x1[j]
            for j in range(i + 1, n):
                S = S + A[i, j] * x0[j]
            x1[i] = (b[i] - S)/A[i, i]

        # criteri di arresto
        residuo = b - np.dot(A, x1)
        residuo_relativo = np.linalg.norm(residuo)/b_norm
        diff_it = np.linalg.norm(x1 - x0)/np.linalg.norm(x1)
        stop = (residuo_relativo < tol) and (diff_it < tol)
        k = k + 1
        x0 = np.copy(x1)

    return x1
