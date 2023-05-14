import statistics
import time
import numpy as np
import matplotlib.pyplot as plot


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
        A_max = abs(A[j, j])
        i_max = j
        for i in range(j * 1, n):
            if abs(A[i, j] > A_max):
                A_max = abs(A[i, j])
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


def sostituzione_indietro(U, b):
    n = len(b)
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        s = np.dot(U[i, i + 1:], x[i + 1:])
        x[i] = (b[i] - s) / U[i, i]
    return x


def calcolo_tempo_errore(T1, T2, Err, Err_P):
    for n in range(5, 200, 5):
        A = (2 * np.random.random((n, n)) - 1) * 3
        x_sol = np.ones((n, 1))
        b = np.dot(A, x_sol)

        start = time.time()
        [U, c] = gauss(A, b)
        end = time.time()
        tempo = end - start
        T1.append(tempo)

        print("gauss ", U)
        print("gauss ", c)

        x = sostituzione_indietro(U, c)

        start = time.time()
        [Z, v] = gauss_pivoting(A, b)

        print("piv ", Z)
        print("piv ", v)

        end = time.time()
        tempo = end - start
        T2.append(tempo)

        x_piv = sostituzione_indietro(Z, v)

        # errore assoluto e relativo per gauss
        ea = np.linalg.norm(x_sol - x)
        er = ea/np.linalg.norm(x_sol)
       # print(er)
        Err.append(er)

        # errore assoluto e relativo per gauss con pivoting
        eap = np.linalg.norm(x_sol - x_piv)
        erp = eap / np.linalg.norm(x_sol)
        #print(erp)
        Err_P.append(erp)

    return T1, T2, Err, Err_P


if __name__ == '__main__':
    T1 = []
    T2 = []
    Err = []
    Err_P = []

    T, TP, Err, Err_P = calcolo_tempo_errore(T1, T2, Err, Err_P)
    x_asses = np.array(range(5, 200, 5))

    plot.figure("Confronto tempi di esecuzione tra Gauss e Gauss con pivoting")
    plot.grid()
    plot.plot(x_asses, T, "y-", label="Eliminazione Gauss")
    plot.plot(x_asses, TP, "g-", label="Eliminazione Gauss Pivoting")
    plot.legend()
    plot.show()

    #print(Err)
   # print(Err_P)

    plot.figure("Confronto errore relativo tra Gauss e Gauss con pivoting")
    plot.grid()
    plot.semilogy(x_asses, Err, "y-", label="Errore relativo Gauss")
    plot.semilogy(x_asses, Err_P, "g-", label="Errore relativo Gauss Pivoting")
    plot.legend()
    plot.show()