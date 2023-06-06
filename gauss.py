import time
import numpy as np
import matplotlib.pyplot as plot


# metodo di eliminazione di Gauss
def gauss(A, b):
    A = np.copy(A)
    b = np.copy(b)
    n = len(A)
    for j in range(n - 1):
        for i in range(j + 1, n):
            m = A[i, j] / A[j, j]
            A[i, j] = 0
            for k in range(j + 1, n):
                A[i, k] = A[i, k] - m * A[j, k]
            b[i] = b[i] - m * b[j]

    return A, b


def partial_pivoting(A, b):
    n = len(b)

    # Creazione della matrice aumentata
    aug_mat = np.column_stack((A, b))

    # Eliminazione gaussiana con pivoting parziale
    for i in range(n):
        # Trova l'indice della riga con il valore massimo nella colonna corrente
        max_row = i
        for j in range(i + 1, n):
            if abs(aug_mat[j, i]) > abs(aug_mat[max_row, i]):
                max_row = j

        # Scambia la riga corrente con la riga con il valore massimo
        aug_mat[[i, max_row], :] = aug_mat[[max_row, i], :]

        # Esegue l'eliminazione gaussiana per ridurre la matrice a una forma triangolare superiore
        for j in range(i + 1, n):
            factor = aug_mat[j, i] / aug_mat[i, i]
            aug_mat[j, :] -= factor * aug_mat[i, :]

    return aug_mat[:, :-1], aug_mat[:, -1]


# metodo di eliminazione di Gauss con pivoting
def gauss_pivoting(A, b):
    A = np.copy(A)
    b = np.copy(b)
    n = len(A)
    for j in range(n - 1):
        # individuazione elemento pivot
        A_max = abs(A[j, j])
        i_max = j
        for i in range(j + 1, n):
            if abs(A[i, j]) > A_max:
                A_max = abs(A[i, j])
                i_max = i

        # eventuale scambio di righe
        if i_max > j:
            for k in range(j, n):
                a_tmp = A[j, k]
                A[j, k] = A[i_max, k]
                A[i_max, k] = a_tmp

            # scambio b
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


def sostituzione_indietro(U, c):
    n = len(c)
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        s = np.dot(U[i, i + 1:], x[i + 1:])
        x[i] = (c[i] - s) / U[i, i]

    return x


def calcolo_tempo_errore(T_G, T_P, Err_G, Err_PI):
    for n in range(5, 200, 5):
        A = (2 * np.random.random((n, n)) - 1) * 3
        x_sol = np.ones((n, 1))
        b = np.dot(A, x_sol)

        start = time.time()
        [U, c] = gauss(A, b)
        end = time.time()
        T_G.append(end - start)

        x = sostituzione_indietro(U, c)

        start = time.time()
        [U, c] = partial_pivoting(A, b)
        end = time.time()
        T2.append(end - start)

        x_piv = sostituzione_indietro(U, c)

        # errore assoluto e relativo per gauss
        err_ass_gauss = np.linalg.norm(x_sol - x)
        err_rel_gauss = err_ass_gauss / np.linalg.norm(x_sol)
        Err.append(err_rel_gauss)

        # errore assoluto e relativo per gauss con pivoting
        err_ass_piv = np.linalg.norm(x_sol - x_piv)
        err_rel_piv = err_ass_piv / np.linalg.norm(x_sol)
        Err_P.append(err_rel_piv)
        print("")

    return T_G, T_P, Err_G, Err_PI


if __name__ == '__main__':
    T1 = []
    T2 = []
    Err = []
    Err_P = []

    T1, T2, Err, Err_P = calcolo_tempo_errore(T1, T2, Err, Err_P)
    x_asses = np.array(range(5, 200, 5))

    plot.figure("Confronto tempi di esecuzione tra Gauss e Gauss con pivoting")
    plot.grid()
    plot.plot(x_asses, T1, "y-", label="Eliminazione Gauss")
    plot.plot(x_asses, T2, "g-", label="Eliminazione Gauss Pivoting")
    plot.legend()
    plot.show()

    plot.figure("Confronto errore relativo tra Gauss e Gauss con pivoting")
    plot.grid()
    plot.semilogy(x_asses, Err, "y-", label="Errore relativo Gauss")
    plot.semilogy(x_asses, Err_P, "g-", label="Errore relativo Gauss Pivoting")
    plot.legend()
    plot.show()
