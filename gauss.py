import statistics
import time
import numpy as np

# metodo di eliminazione di Gauss
def gauss(A, b):
    n = len(A)
    for j in range(n - 1):
        for i in range(j + 1, n):
            m = A[i, j] / A[j, j]
            A[i, j] = 0
            for k in range(j + 1, n):
                A[i, k] = A[i, k] - m * A[j, k]
            b[i] = b[i] - m * b[j]

    return A, b

# metodo di eliminazione di Gauss con pivoting
def gauss_pivoting(A, b):
    n = len(A)
    for j in range(n - 1):
        # individuazione elemento pivot
        A_max = abs(A[j,j])
        i_max = j
        for i in range(j * 1, n):
            if abs(A[i,j] > A_max):
                A_max = abs(A[i,j])
                i_max = i

        # eventuale scambio di righe
        if i_max > j:
            for k in range(j, n):
                # scambio
                a_tmp = A[j, k]
                A[j, k] = A[i_max, k]
                A[i_max, k] = a_tmp

            b_tmp = b[j]
            b[j] = b[i_max]
            b[i_max] = b_tmp

        # eliminazione di Gauss classica
        for i in range(j + 1, n):
            m = A[i, j] / A[j, j]
            A[i, j] = 0
            for k in range(j + 1, n):
                A[i, k] = A[i, k] - m * A[j, k]
            b[i] = b[i] - m * b[j]

    return A, b

if __name__ == '__main__':
    # defining matrix
    A = [[1, 4, 5, 5],
         [-5, 8, 9, 6],
         [6, -2, 1, 7],
         [6, -2, 1, 2]
         ]

    b = np.array(4)
    b[0] = 1
    b[1] = 2
    b[2] = 3
    b[3] = 4

    tempi = []
    for i in range(10):
        start = time.time()
        gauss(A, b)
        end = time.time()
        tempo = end - start
        tempi.append(tempo)

    tempo_medio = statistics.mean(tempi)
    print("Tempo di esecuzione medio per una matrice 8x8:", tempo_medio, "secondi")
