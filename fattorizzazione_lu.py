import statistics
import time
import numpy as np


def fattorizzazione_lu(A):
    A = np.copy(A)
    n = len(A)
    L = np.zeros([n, n])
    for j in range(n - 1):
        L[j, j] = 1
        for i in range(j + 1, n):
            m = A[i, j] / A[j, j]
            L[i, j] = m
            A[i, j] = 0
            for k in range(j + 1, n):
                A[i, k] = A[i, k] - m * A[j, k]

    lower = np.tril(A, -1) + np.eye(n, n)
    upper = np.triu(A)
    return lower, upper


def fattorizzazione_lu_ottimizzata(A):
    A = np.copy(A)
    n = len(A)
    for j in range(n - 1):
        for i in range(j + 1, n):
            A[i, j] = A[i, j] / A[j, j]
            for k in range(j + 1, n):
                A[i, k] = A[i, k] - A[i, j] * A[j, k]

    lower = np.tril(A, -1) + np.eye(n, n)
    upper = np.triu(A)
    return lower, upper

def fattorizzazione_lu_pivot(A):
    A = np.copy(A)
    n = len(A)
    indice = np.array(range(n))
    for j in range(n - 1):

        # individuazione dell ’elemento pivot
        i_piv = np.argmax(abs(A[j:n, j])) + j

        # eventuale scambio di righe
        if i_piv > j:
            for k in range(n):
                A[i_piv, k], A[j, k] = A[j, k], A[i_piv, k]
            indice[i_piv], indice[j] = indice[j], indice[i_piv]

        # eliminazione elementi sulla colonna j
        for i in range(j + 1, n):
            A[i, j] = A[i, j]/A[j, j]
            for k in range(j + 1, n):
                A[i, k] = A[1, k] - A[i, j] * A[j, k]

    lower = np.tril(A, -1) + np.eye(n, n)
    upper = np.triu(A)
    return lower, upper, indice


def fattorizzazione_lu_pivot_ottimizzata(A):
    A = np.copy(A)
    n = len(A)
    indice = np.array(range(n))
    for j in range(n - 1):

        # individuazione dell ’elemento pivot
        i_piv = np.argmax(abs(A[j:n, j])) + j

        # eventuale scambio di righe
        if i_piv > j:
            A[[i_piv, j], :] = A[[j, i_piv], :]
            indice[[i_piv, j]] = indice[[j, i_piv]]

        # eliminazione elementi sulla colonna j
        for i in range(j + 1, n):
            A[i, j] = A[i, j]/A[j, j]
            A[i, j + 1: n] = A[i, j + 1: n] - A[i, j] * A[j, j + 1: n]

    lower = np.tril(A, -1) + np.eye(n, n)
    upper = np.triu(A)
    return lower, upper, indice


if __name__ == '__main__':
    # defining matrix
    n = 200
    A = (2*np.random.random((n, n)) - 1) * 3

    times = []
    for i in range(10):
        start = time.time()
        fattorizzazione_lu(A)
        end = time.time()
        times.append(end - start)

    tempo_medio = statistics.mean(times)
    print("Tempo di esecuzione medio fattorizzazione LU per una matrice ", n, "x", n, ": ", tempo_medio, "secondi")

    times = []
    for i in range(10):
        start = time.time()
        fattorizzazione_lu_ottimizzata(A)
        end = time.time()
        times.append(end - start)

    tempo_medio = statistics.mean(times)
    print("Tempo di esecuzione medio fattorizzazione LU ottimizzata per una matrice ", n, "x", n, ": ", tempo_medio, "secondi")

    times = []
    for i in range(10):
        start = time.time()
        fattorizzazione_lu_pivot(A)
        end = time.time()
        times.append(end - start)

    tempo_medio = statistics.mean(times)
    print("Tempo di esecuzione medio fattorizzazione LU con pivoting per una matrice ", n, "x", n, ": ", tempo_medio, "secondi")

    times = []
    for i in range(10):
        start = time.time()
        fattorizzazione_lu_pivot_ottimizzata(A)
        end = time.time()
        times.append(end - start)

    tempo_medio = statistics.mean(times)
    print("Tempo di esecuzione medio fattorizzazione LU con pivoting ottimizzata per una matrice ", n, "x", n, ": ", tempo_medio, "secondi")